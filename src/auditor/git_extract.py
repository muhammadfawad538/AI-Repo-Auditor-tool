from __future__ import annotations

import subprocess
import tempfile
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

try:
    import git

    HAS_GITPYTHON = True
except ImportError:
    HAS_GITPYTHON = False


@dataclass
class Commit:
    sha: str
    author: str
    author_email: str
    date: datetime
    message: str
    diff: str
    files_changed: int
    insertions: int
    deletions: int


def resolve_repo(path_or_url: str) -> Path:
    if path_or_url.startswith(("http://", "https://", "git@")):
        tmp_dir = Path(tempfile.mkdtemp(prefix="auditor-clone-"))
        subprocess.run(
            ["git", "clone", "--quiet", path_or_url, str(tmp_dir)], check=True
        )
        return tmp_dir
    return Path(path_or_url).resolve()


def extract_commits(
    repo_path: Path, since: str | None = None, max_commits: int | None = None
) -> list[Commit]:
    if HAS_GITPYTHON:
        return _extract_with_gitpython(repo_path, since, max_commits)
    return _extract_with_subprocess(repo_path, since, max_commits)


def _extract_with_gitpython(
    repo_path: Path, since: str | None, max_commits: int | None
) -> list[Commit]:
    repo = git.Repo(repo_path)
    kwargs: dict = {}
    if since:
        kwargs["since"] = since
    if max_commits:
        kwargs["max_count"] = max_commits

    commits = []
    for c in repo.iter_commits("HEAD", **kwargs):
        diff_text = repo.git.show(c.hexsha, "--format=")
        stats = c.stats.total
        commits.append(
            Commit(
                sha=c.hexsha,
                author=c.author.name or "",
                author_email=c.author.email or "",
                date=datetime.fromtimestamp(c.committed_date),
                message=c.message.strip(),
                diff=diff_text,
                files_changed=stats.get("files", 0),
                insertions=stats.get("insertions", 0),
                deletions=stats.get("deletions", 0),
            )
        )
    return commits


def _run(repo_path: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(repo_path), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=True,
    ).stdout


def _parse_shortstat(stat: str) -> tuple[int, int, int]:
    insertions = deletions = files_changed = 0
    line = stat.strip()
    if not line:
        return insertions, deletions, files_changed
    for part in line.split(","):
        part = part.strip()
        if "file" in part:
            files_changed = int(part.split()[0])
        elif "insertion" in part:
            insertions = int(part.split()[0])
        elif "deletion" in part:
            deletions = int(part.split()[0])
    return insertions, deletions, files_changed


def _extract_with_subprocess(
    repo_path: Path, since: str | None, max_commits: int | None
) -> list[Commit]:
    log_args = ["log", "--pretty=format:%H%x1f%an%x1f%ae%x1f%at%x1f%B%x1e"]
    if since:
        log_args.append(f"--since={since}")
    if max_commits:
        log_args.append(f"-n{max_commits}")

    out = _run(repo_path, *log_args)
    commits = []
    for record in out.split("\x1e"):
        record = record.strip("\n")
        if not record:
            continue
        sha, author, email, ts, message = record.split("\x1f")
        stat = _run(repo_path, "show", sha, "--format=", "--shortstat")
        insertions, deletions, files_changed = _parse_shortstat(stat)
        diff = _run(repo_path, "show", sha, "--format=")
        commits.append(
            Commit(
                sha=sha,
                author=author,
                author_email=email,
                date=datetime.fromtimestamp(int(ts)),
                message=message.strip(),
                diff=diff,
                files_changed=files_changed,
                insertions=insertions,
                deletions=deletions,
            )
        )
    return commits

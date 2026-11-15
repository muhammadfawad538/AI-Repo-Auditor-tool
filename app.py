from __future__ import annotations

import os

import streamlit as st
from dotenv import load_dotenv

from auditor.git_extract import extract_commits, resolve_repo
from auditor.heuristics import score_heuristics
from auditor.investigator import investigate_commit
from auditor.llm_judge import score_with_llm
from auditor.report import BAND_DESCRIPTIONS, DISAGREEMENT_THRESHOLD, VERDICT_BANDS, verdict_label

load_dotenv()

LOGO_PATH = "assets/must_company_logo.png"

st.set_page_config(page_title="AI Usage Authenticity Auditor", layout="wide")
if os.path.exists(LOGO_PATH):
    st.logo(LOGO_PATH)
header_col1, header_col2 = st.columns([1, 8])
if os.path.exists(LOGO_PATH):
    header_col1.image(LOGO_PATH, width=72)
header_col2.title("AI Usage Authenticity Auditor")
st.caption("Thin Streamlit wrapper over the `audit` CLI — same heuristic + LLM judge layers, no logic duplicated.")
st.caption("Built for the MUST Company AI Native Super Engineer quest.")


def _sample(commits: list, n: int) -> list:
    if n <= 0 or n >= len(commits):
        return commits
    step = len(commits) / n
    return [commits[int(i * step)] for i in range(n)]


with st.form("audit_form"):
    repo = st.text_input("Repo path or URL", placeholder=r"C:\path\to\repo  or  https://github.com/org/repo")
    col1, col2 = st.columns(2)
    since = col1.text_input("Since (optional)", placeholder="2024-01-01")
    until = col2.text_input("Until (optional)", placeholder="2015-01-01")
    max_llm = st.number_input(
        "Max commits sent to the LLM judge (cost control; 0 = no limit)",
        min_value=0, value=20, step=5,
    )
    investigate = st.checkbox("Investigate disagreements with the agent (extra API calls, ~2 per commit)")
    max_investigations = st.number_input("Max commits to investigate", min_value=1, value=3, step=1)
    submitted = st.form_submit_button("Run Audit")

if submitted:
    if not repo.strip():
        st.error("Enter a repo path or URL.")
        st.stop()

    with st.spinner("Extracting commits..."):
        repo_path = resolve_repo(repo.strip())
        commits = extract_commits(repo_path, since=since.strip() or None, until=until.strip() or None)

    if not commits:
        st.warning("No commits found for that repo/date range.")
        st.stop()

    st.write(f"Extracted **{len(commits)}** commit(s).")
    heuristic_results = score_heuristics(commits)

    judge_results = {}
    if not os.environ.get("OPENAI_API_KEY"):
        st.warning("OPENAI_API_KEY not set — showing heuristic scores only.")
    else:
        llm_commits = _sample(commits, int(max_llm))
        if len(llm_commits) < len(commits):
            st.info(f"Sampling {len(llm_commits)} of {len(commits)} commits for the LLM judge to control cost.")
        else:
            st.info(f"Sending all {len(llm_commits)} commit(s) to the LLM judge.")

        progress = st.progress(0.0)
        for i, commit in enumerate(llm_commits, 1):
            try:
                judge_results[commit.sha] = score_with_llm(commit)
            except Exception as e:
                judge_results[commit.sha] = None
                st.caption(f"LLM judge failed on `{commit.sha[:10]}`: {e}")
            progress.progress(i / len(llm_commits))
        progress.empty()

    investigations = {}
    if investigate and judge_results:
        flagged = [
            c for c in commits
            if (j := judge_results.get(c.sha)) is not None
            and abs(heuristic_results[c.sha].score - j.score) >= DISAGREEMENT_THRESHOLD
        ][: int(max_investigations)]
        if not flagged:
            st.info("No disagreeing commits to investigate.")
        for i, c in enumerate(flagged, 1):
            with st.spinner(f"Agent investigating {c.sha[:10]} ({i}/{len(flagged)})..."):
                try:
                    investigations[c.sha] = investigate_commit(
                        c, commits, repo_path, heuristic_results[c.sha], judge_results[c.sha]
                    )
                except Exception as e:
                    st.caption(f"Investigation failed on `{c.sha[:10]}`: {e}")

    rows = []
    disagreements = 0
    for c in commits:
        h = heuristic_results[c.sha]
        j = judge_results.get(c.sha)
        j_score = j.score if j else None
        inv = investigations.get(c.sha)
        resolved = inv.score if inv and inv.score is not None else None
        if resolved is not None:
            combined = round(resolved, 1)
        else:
            combined = round((h.score + j_score) / 2, 1) if j_score is not None else round(h.score, 1)
        disagree = j_score is not None and abs(h.score - j_score) >= DISAGREEMENT_THRESHOLD
        disagreements += int(disagree)
        first_line = c.message.splitlines()[0] if c.message else ""
        snippet = (j.reasoning[:160] + "…") if j and j.reasoning and len(j.reasoning) > 160 else (j.reasoning if j else "")
        rows.append({
            "Commit": c.sha[:10],
            "Message": first_line[:70] + ("…" if len(first_line) > 70 else ""),
            "Heuristic": round(h.score, 1),
            "LLM Judge": round(j_score, 1) if j_score is not None else None,
            "Combined": combined,
            "Resolved (agent)": round(resolved, 1) if resolved is not None else None,
            "Reasoning": snippet,
            "Disagreement": "⚠️ Yes" if disagree else "",
        })

    rows.sort(key=lambda r: r["Combined"], reverse=True)

    # Form widgets reset `submitted` to False on every later rerun (e.g. the
    # commit-detail selectbox below), so the results have to live in
    # session_state or picking a commit would wipe the whole page.
    st.session_state["audit_result"] = {
        "commits": commits,
        "heuristic_results": heuristic_results,
        "judge_results": judge_results,
        "investigations": investigations,
        "rows": rows,
        "disagreements": disagreements,
    }

if "audit_result" in st.session_state:
    result = st.session_state["audit_result"]
    commits = result["commits"]
    heuristic_results = result["heuristic_results"]
    judge_results = result["judge_results"]
    investigations = result["investigations"]
    rows = result["rows"]
    disagreements = result["disagreements"]

    overall_score = sum(r["Combined"] for r in rows) / len(rows)
    st.markdown(f"### Verdict: {verdict_label(overall_score)} ({overall_score:.1f}/100)")
    st.caption(
        "Based on commit patterns and AI judge reasoning — not a certainty. "
        "See Known Limitations in the README before treating this as proof."
    )
    with st.expander("What do these labels mean?"):
        lower = 0
        band_rows = []
        for upper, label in VERDICT_BANDS:
            band_rows.append({"Score range": f"{lower}-{upper}", "Label": label, "Meaning": BAND_DESCRIPTIONS[label]})
            lower = upper + 1
        st.table(band_rows)

    if disagreements > 0:
        st.warning(
            f"⚠️ {disagreements} commit(s) show the heuristic and LLM-judge layers disagreeing by "
            f">={DISAGREEMENT_THRESHOLD:.0f} points — the blended score is less trustworthy there; "
            "look at the commit directly (see **Commit detail** below)."
        )

    st.subheader("Per-commit scores")
    st.dataframe(rows, width="stretch", hide_index=True)

    st.subheader("Commit detail")
    selected = st.selectbox("Pick a commit to see its full reasoning", [r["Commit"] for r in rows])
    selected_commit = next(c for c in commits if c.sha.startswith(selected))
    h_detail = heuristic_results[selected_commit.sha]
    j_detail = judge_results.get(selected_commit.sha)

    with st.expander(f"`{selected}` — {selected_commit.message.splitlines()[0]}", expanded=True):
        st.write("**Heuristic breakdown:**")
        for sig in h_detail.signals:
            st.write(f"- *{sig.name}* ({sig.score:.0f}/100): {sig.reasoning}")
        if j_detail:
            st.write(f"**LLM judge score:** {j_detail.score:.0f}/100")
            st.text_area("Full reasoning", j_detail.reasoning, height=200, disabled=True)
            if j_detail.key_signals:
                st.write("**Key signals:** " + ", ".join(j_detail.key_signals))
        else:
            st.write("_LLM judge was not run for this commit._")
        inv_detail = investigations.get(selected_commit.sha)
        if inv_detail and inv_detail.score is not None:
            st.write(f"**Agent ruling: {inv_detail.score:.0f}/100** (closer layer: {inv_detail.closer_layer})")
            st.write(inv_detail.reasoning)
            for item in inv_detail.evidence:
                st.write(f"- Evidence: {item}")
            st.write("**Tool trail:**")
            for i, step in enumerate(inv_detail.steps, 1):
                args = ", ".join(f"{k}={v}" for k, v in step["args"].items())
                st.write(f"{i}. `{step['tool']}({args})`")

    st.subheader("Aggregate summary")
    judged = [r for r in rows if r["LLM Judge"] is not None]
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Overall repo score", f"{overall_score:.1f}/100")
    col2.metric("Commits analyzed", len(rows))
    col3.metric("Commits judged by LLM", len(judged))
    col4.metric(f"Layer disagreements (>={DISAGREEMENT_THRESHOLD:.0f} pts)", disagreements)

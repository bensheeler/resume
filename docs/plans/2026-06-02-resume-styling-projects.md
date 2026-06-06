# Resume Styling And Projects Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Update the generated Typst resume to better match the original PDF style, render projects, and make the build workflow obvious.

**Architecture:** Keep `resume.yaml` as the source of truth and `build_resume.py` as the adapter from YAML to Typst. Use `basic-resume` for document setup and headings, but render experience and projects with custom Typst markup for better layout control.

**Tech Stack:** Python, PyYAML, Typst, Typst `basic-resume`

---

### Task 1: Add Failing Renderer Tests

**Files:**
- Modify: `/Users/bensheeler/code/resume/tests/test_build_resume.py`

**Step 1: Update the experience rendering test**

Assert each role renders the company and title on one line with the company bolded.

**Step 2: Add a projects rendering test**

Assert a sample project renders its name, link, summary, highlights, and tech list.

**Step 3: Run tests to verify red**

Run: `python3 -m unittest tests/test_build_resume.py`

Expected: FAIL because the renderer still emits `#work(...)` blocks and lacks `render_projects`.

### Task 2: Implement Custom Rendering

**Files:**
- Modify: `/Users/bensheeler/code/resume/build_resume.py`

**Step 1: Change the generated font**

Set `font: "Georgia"` in `render_header`.

**Step 2: Replace `#work(...)` rendering**

Emit custom Typst lines with bold company, role on the same line, dates/location grid, bullets, tech, and a small vertical gap.

**Step 3: Add `render_projects`**

Render optional `projects` only when present.

**Step 4: Include projects in `render_resume`**

Append the project section between experience and education when `projects` exists.

### Task 3: Add Workflow Helpers

**Files:**
- Modify: `/Users/bensheeler/code/resume/resume.yaml`
- Create: `/Users/bensheeler/code/resume/Makefile`
- Create: `/Users/bensheeler/code/resume/README.md`

**Step 1: Add sample project YAML**

Add a `projects` section with a placeholder Resume Builder project.

**Step 2: Add `make build`**

Create a Makefile target that runs `python3 build_resume.py`.

**Step 3: Document rebuild behavior**

Explain that edits to `resume.yaml` require rerunning `make build` or `python3 build_resume.py`.

### Task 4: Verify

**Files:**
- Generated: `/Users/bensheeler/code/resume/resume.typ`
- Generated: `/Users/bensheeler/code/resume/resume.pdf`

**Step 1: Run unit tests**

Run: `python3 -m unittest tests/test_build_resume.py`

Expected: OK.

**Step 2: Run full build**

Run: `python3 build_resume.py`

Expected: exit 0 and regenerated `resume.pdf`.

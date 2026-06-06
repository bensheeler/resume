# Resume YAML Schema Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Restructure `resume.yaml` to use the approved nested company and role schema while preserving the current resume content.

**Architecture:** Keep the source of truth in a single YAML file with top-level `basics`, `experience`, and `education` sections. Each experience item will represent a company, and each company will contain a `roles` array so future promotions at the same employer can be grouped naturally.

**Tech Stack:** YAML

---

### Task 1: Update Experience Schema

**Files:**
- Modify: `/Users/bensheeler/code/resume/resume.yaml`

**Step 1: Review the existing YAML content**

Read `/Users/bensheeler/code/resume/resume.yaml` and identify the current flat experience entries.

**Step 2: Rewrite each experience item to use `roles`**

Move each job title, date range, bullet list, and tech list into a single-item `roles` array under its company.

**Step 3: Preserve existing resume content**

Keep the same real-world content from the current resume while changing only the shape needed for the new schema.

**Step 4: Verify the YAML structure**

Read `/Users/bensheeler/code/resume/resume.yaml` and confirm the top-level sections and nested `roles` arrays are present for every experience entry.

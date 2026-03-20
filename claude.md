# CLAUDE.md — Project Rules & Conventions

This file defines how Claude should behave across all tasks in this repository.
Read it fully before writing, editing, or reviewing any code.

---

## Context Files

### Calculations & Data Reference
<!-- Replace the path below with the actual file location when known -->
Always read `@[PATH_TO_CONSTANTS_FILE]` before performing any calculations,
generating values, or referencing project-specific numbers, thresholds, or
configuration. Do not hardcode values that exist in this file.

### Visual Template
<!-- Replace the path below with the actual template file when known -->
The file `@[PATH_TO_TEMPLATE_HTML]` is the visual reference for this project.
Match its style loosely — adopt its color palette, font choices, spacing rhythm,
and component shapes, but do not copy it verbatim. The goal is visual family
resemblance, not pixel-perfect duplication.

---

## Page Synthesis

When creating or editing any page, Claude must ensure it feels like part of the
same product as every other page in the repo. This means:

### Navigation & Layout
- Every page must include the shared header, navigation, and footer.
- Use the same nav structure and link order as the template file.
- Do not invent new layout regions that don't exist in the template.

### Color & Typography
- Use only the color palette established in the template. Do not introduce new
  colors unless explicitly asked.
- Match font families, weights, and size scales from the template.
- Maintain the same heading hierarchy (h1 → h2 → h3) used across the project.

### Spacing & Components
- Match the padding, margin, and gap patterns visible in the template.
- Reuse existing component patterns (cards, buttons, inputs, sections) rather
  than creating new ones from scratch.
- When a new component is needed, model it after the closest existing pattern.

---

## Offline & PWA Requirements

- Every page must register a service worker for offline support.
- Use a cache-first strategy for local assets.
- Use stale-while-revalidate for remote images.
- Provide a visible fallback if a remote image fails to load offline.
- All remote image sources must support CORS.

---

## General Conventions

- Write clean, readable code with descriptive variable names.
- Prefer vanilla HTML, CSS, and JavaScript unless the project already uses a
  framework.
- No hardcoded magic numbers — reference the constants file.
- Keep files focused. One page or component per file.
- Update this file if you introduce a new convention the team should follow.

---

## Placeholders to Fill In

Before this file is production-ready, replace the following:

| Placeholder                  | What to put here                            |
|------------------------------|---------------------------------------------|
| `[PATH_TO_CONSTANTS_FILE]`   | Path to the data/calculations context file  |
| `[PATH_TO_TEMPLATE_HTML]`    | Path to the visual reference HTML file      |

# Repo rules for Codex

This repository is a public skill repo. Before finishing any change:

1. **Review the intro.** Open `README.md` (and update `README.zh-CN.md` and other language mirrors when the change is user-visible). Keep the hook sharp, the gallery current, install instructions accurate, and all links/badges working.
2. **Optimize for discoverability.** The goal is stars and adoption. If a change adds a capability, feature, or asset, reflect it in the README feature list and table of contents; add or refresh screenshots when visuals change.
3. **Verify before pushing.** Run `quick_validate.py` on the skill folder, check for leaked API keys, and confirm remote tree matches local HEAD after push.
4. **Keep sync.** Local installed copy (`~/.codex/skills/premium-website-design`) and the curated PR package under `/tmp/curated-pkg` should stay in sync with this repo when skill files change.

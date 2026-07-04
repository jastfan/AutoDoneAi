# Contributing to AutoDoneAi

Thanks for considering a contribution! AutoDoneAi is intentionally a small, single-script project (`autojob.py` as the Flask backend + vanilla-JS frontend, `ai_enhance.py` for the AI enhancement pass), so please keep changes focused and avoid introducing a build step unless discussed first.

## Ways to help

- 🐛 Report bugs via [Issues](https://github.com/jastfan/AutoDoneAi/issues) — include your OS, Python version, browser, and the platform/URL type you tested
- 💡 Suggest features — open an issue with the `enhancement` label
- 🔧 Pick up a [`good first issue`](https://github.com/jastfan/AutoDoneAi/labels/good%20first%20issue) if you're new to the codebase
- 🌍 Test and report back on non-YouTube sources (Instagram, Facebook, etc.) — this is a high-value, low-code way to help right now
- 📝 Improve docs, add screenshots/GIFs, or write a usage guide

## Development setup

```bash
git clone https://github.com/jastfan/AutoDoneAi.git
cd AutoDoneAi
pip install -r requirements.txt
python autojob.py
```

## Submitting a change

1. Fork the repo and create a branch: `git checkout -b fix/short-description`
2. Make your change, test it locally end-to-end (fetch → cut → edit → enhance → export)
3. Open a PR with a clear description of what changed and why
4. Be responsive to review feedback — small, focused PRs merge fastest

## Code style

- Keep the single-file architecture unless a change genuinely needs a new module
- Match the existing naming and comment style
- No new frontend build tools/frameworks — vanilla HTML/CSS/JS only
- If you touch `ai_enhance.py`, keep model loading lazy (models should load once, not per-frame)

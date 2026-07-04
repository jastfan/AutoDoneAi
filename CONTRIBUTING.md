# Contributing to Shorts Studio

Thanks for considering a contribution! This project is small and single-file by design (one Flask backend + one vanilla-JS frontend), so please keep changes focused and avoid introducing a build step unless discussed first.

## Ways to help

- 🐛 Report bugs via [Issues](../../issues) — include your OS, Python version, and steps to reproduce
- 💡 Suggest features — open an issue with the `enhancement` label
- 🔧 Pick up a [`good first issue`](../../labels/good%20first%20issue) if you're new to the codebase
- 📝 Improve docs, add screenshots/GIFs, or write a usage guide

## Development setup

```bash
git clone https://github.com/<your-username>/shorts-studio.git
cd shorts-studio
pip install -r requirements.txt
python shortvideo.py
```

## Submitting a change

1. Fork the repo and create a branch: `git checkout -b fix/short-description`
2. Make your change, test it locally end-to-end (fetch → cut → edit → export)
3. Open a PR with a clear description of what changed and why
4. Be responsive to review feedback — small, focused PRs merge fastest

## Code style

- Keep the single-file architecture unless a change genuinely needs a new module
- Match the existing naming and comment style
- No new frontend build tools/frameworks — vanilla HTML/CSS/JS only

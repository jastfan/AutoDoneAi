<div align="center">

# 🎬 Shorts Studio

**Turn any YouTube video into ready-to-post vertical Shorts — cut, edit, and export, all from your browser, all on your own machine.**

[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-backend-black.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

[Features](#-features) • [Quick Start](#-quick-start) • [How It Works](#-how-it-works) • [Roadmap](#-roadmap) • [Contributing](#-contributing)

<!-- Replace this line with an actual GIF/screenshot: assets/demo.gif -->
![demo](assets/demo.gif)

</div>

---

## Why Shorts Studio?

Most "YouTube to Shorts" tools either lock you into a paid SaaS or dump a single auto-cut file with no control. Shorts Studio is different:

- **100% local** — your video never leaves your machine, no cloud upload, no subscription.
- **Live in-browser editor** — tweak speed, zoom, color grade, captions, logo, and hide-regions per clip before anything is written to disk.
- **Built-in AI voiceover** — Hindi/English text-to-speech via Edge TTS or gTTS, no extra API keys.
- **Fast by design** — parallel clip cutting, ultrafast proxy previews, and a stream-copy export path that skips re-encoding when nothing changed.

## ✨ Features

- 🔗 Paste a YouTube link → auto-detects the best available quality and pulls video + audio streams
- ✂️ **Auto mode**: splits the full video into fixed-length vertical (9:16) shorts
- 🎯 **Manual mode**: pick your own start/end ranges
- ⚡ Parallel clip cutting (`ThreadPoolExecutor`) — cuts don't wait on each other
- 🖊️ Per-clip live editing: speed, zoom, mute/replace audio, text overlays, logo, blur/black/emoji hide-regions, rectangle/circle/arrow shapes
- 🎨 One-click color presets (Vivid, Cinematic, Moody, Vintage VHS, Warm Glow, Cool Blue)
- 🗣️ AI voiceover: Edge TTS (Hindi/English, multiple voices) and gTTS fallback
- 🎵 Drop-in background music library (`audio/` folder)
- 💾 Smart export: stream-copies the proxy file instead of re-encoding when no edits changed the output
- 📥 Batch download manager for all exported clips

## 🚀 Quick Start

```bash
git clone https://github.com/<your-username>/shorts-studio.git
cd shorts-studio
pip install -r requirements.txt
python shortvideo.py
```

The app opens automatically at `http://127.0.0.1:5789`.

> **Tip:** drop `.mp3` files into the `audio/` folder before launching to use them as background music inside the editor.

### Requirements
- Python 3.9+
- ffmpeg (bundled via `imageio-ffmpeg`, no separate install needed)
- A modern browser (Chrome/Edge/Firefox)

## 🛠 How It Works

1. **Resolve** — `yt-dlp` locates the best video/audio stream for the URL (with cookie fallbacks for restricted videos).
2. **Cut** — the video is split into short segments in parallel using fast preview-quality encodes.
3. **Edit** — each short opens in the browser UI for live-preview edits (nothing is re-encoded yet).
4. **Export** — on Save, your edits are baked in; unedited clips are stream-copied for a near-instant export.

## 🗺 Roadmap

- [ ] One-click auto-captions (Whisper-based)
- [ ] Batch export presets (save a "style" and apply to a whole video)
- [ ] Docker image for one-command setup
- [ ] Optional cloud storage export (Drive/S3)
- [ ] Multi-language UI

Have an idea? [Open an issue](../../issues) or check [`good first issue`](../../labels/good%20first%20issue) to contribute.

## 🤝 Contributing

Contributions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Bug reports, feature ideas, and PRs all help.

## 📄 License

MIT — see [LICENSE](LICENSE).

---

<div align="center">
If this saved you time, a ⭐ on the repo helps others find it.
</div>

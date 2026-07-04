<div align="center">

# 🤖 AutoDoneAi

**Paste a video link. Get edited, HD-enhanced, ready-to-post vertical Shorts — cut, upscaled, voiced-over, and exported, all locally in your browser.**

A local YouTube Shorts / Reels automation studio: powered by `yt-dlp` for fetching, `ffmpeg` for cutting and color, and AI face-restoration/upscaling (GFPGAN + Real-ESRGAN) for HD output — one Python script, no cloud, no subscription.

[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-backend-black.svg)](https://flask.palletsprojects.com/)
[![yt-dlp](https://img.shields.io/badge/powered%20by-yt--dlp-red.svg)](https://github.com/yt-dlp/yt-dlp)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

[Features](#-features) • [Quick Start](#-quick-start) • [How It Works](#-how-it-works) • [Roadmap](#-roadmap) • [Contributing](#-contributing)

<!-- Replace with a real 10-15s GIF of the editor in action -->
![demo](assets/demo.gif)

</div>

---

## Why AutoDoneAi?

Most "video to Shorts" tools either lock you into a paid SaaS, upload your footage to someone else's server, or hand you one flat auto-cut file with zero control. AutoDoneAi is different:

- **100% local** — nothing you process leaves your machine. No account, no cloud storage, no subscription.
- **One script, full pipeline** — fetch → cut → live-edit → AI-enhance → export, all in a single Flask app with a modern browser UI (no build step).
- **Real editing, not just cutting** — per-clip speed, zoom, color grade, captions, logo, hide-regions, and AI voiceover before anything is written to disk.
- **AI HD Enhance** — optional GFPGAN face-restoration + Real-ESRGAN upscaling pass so clips stay sharp instead of pixelating when zoomed or upscaled.
- **Built on `yt-dlp`** — the same engine that powers most modern video-archival tools, so it isn't limited to a single site by design.

## ✨ Features

- 🔗 Paste a video link → auto-resolves the best available video + audio quality
- 🧠 Smart bot-detection bypass — tries cookies, browser sessions, and fallback clients automatically so fetches don't get blocked
- ✂️ **Auto mode**: splits the full video into fixed-length vertical (9:16) shorts
- 🎯 **Manual mode**: pick your own start/end ranges
- ⚡ Parallel clip cutting — cuts don't wait on each other
- 🖊️ Per-clip live editing: speed, zoom, mute/replace audio, text overlays, logo, blur/black/emoji hide-regions, rectangle/circle/arrow shapes
- 🎨 One-click color presets (Vivid, Cinematic, Moody, Vintage VHS, Warm Glow, Cool Blue)
- 🪄 **AI HD Enhance** — GFPGAN face restoration + Real-ESRGAN upscaling, denoise/detail pass (weights auto-download on first use)
- 🗣️ AI voiceover: Edge TTS (Hindi/English, multiple voices) + gTTS fallback
- 🎵 Drop-in background music library (`audio/` folder)
- 💾 Smart export — stream-copies unedited clips instead of re-encoding for near-instant Save
- 📥 Batch download manager for all exported clips

## 🚀 Quick Start

```bash
git clone https://github.com/jastfan/AutoDoneAi.git
cd AutoDoneAi
pip install -r requirements.txt
python autojob.py
```

The app opens automatically at `http://127.0.0.1:5789`.

> **Tip:** drop `.mp3` files into `audio/` before launching to use them as background music inside the editor.
> **Note on AI Enhance:** the first time you enable HD Enhance, it auto-downloads the GFPGAN and Real-ESRGAN model weights (one-time, a few hundred MB). This needs a working internet connection once; after that it runs fully offline.

### Requirements
- Python 3.9+
- ffmpeg (bundled via `imageio-ffmpeg`, no separate install needed)
- A modern browser (Chrome/Edge/Firefox)
- ~2GB free disk space if you plan to use AI HD Enhance (model weights)

## 🛠 How It Works

1. **Resolve** — `yt-dlp` locates the best video/audio stream for the URL, with automatic cookie/session fallbacks if the first attempt is blocked.
2. **Cut** — the video is split into short segments in parallel using fast preview-quality encodes.
3. **Edit** — each clip opens in the browser UI for live-preview edits (nothing is re-encoded yet).
4. **Enhance** *(optional)* — GFPGAN + Real-ESRGAN run a face-restoration/upscale pass on the clip.
5. **Export** — on Save, edits are baked in; unedited clips are stream-copied for a near-instant export.

## 🌍 Beyond YouTube

Under the hood, AutoDoneAi runs on `yt-dlp`, which supports 1,800+ sites — so pasting a link from Instagram, Facebook, or many other platforms will often work out of the box. The bot-detection bypass and cookie-fallback logic in this build are currently tuned specifically for YouTube; other platforms aren't yet tested to the same degree, and cookie handling for platform-locked content may need extra setup. Wider, tested multi-platform support is an active roadmap item — see below.

## 🗺 Roadmap

- [ ] Tested, documented Instagram + Facebook fetch flows
- [ ] Local file upload (edit your own PC videos without a URL)
- [ ] video2ppt-style module — extract slides/key-frames from lecture or webinar videos
- [ ] One-click auto-captions (Whisper-based)
- [ ] Docker image for one-command setup
- [ ] Multi-language UI

Have an idea? [Open an issue](https://github.com/jastfan/AutoDoneAi/issues) or check [`good first issue`](https://github.com/jastfan/AutoDoneAi/labels/good%20first%20issue) to contribute.

## 🤝 Contributing

Contributions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Bug reports, feature ideas, and PRs all help.

## 📄 License

MIT — see [LICENSE](LICENSE).

---

<div align="center">
If this saved you time, a ⭐ on the repo helps others find it.
</div>

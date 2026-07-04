# ai_enhance.py
import os
import urllib.request
from pathlib import Path

import cv2
import numpy as np

WEIGHTS_DIR = Path(__file__).resolve().parent / "weights"
WEIGHTS_DIR.mkdir(exist_ok=True)

MODEL_URLS = {
    "GFPGANv1.4.pth": "https://github.com/TencentARC/GFPGAN/releases/download/v1.3.4/GFPGANv1.4.pth",
    "RealESRGAN_x2plus.pth": "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.1/RealESRGAN_x2plus.pth",
}

_face_enhancer = None
_bg_upsampler = None


def _download_with_progress(url, dest_path):
    print(f"[AI Enhance] Downloading {dest_path.name} (one-time setup)...")

    def _hook(count, block_size, total_size):
        if total_size <= 0:
            return
        pct = min(100, int(count * block_size * 100 / total_size))
        print(f"\r[AI Enhance] {dest_path.name}: {pct}%", end="", flush=True)

    tmp_path = dest_path.with_suffix(".part")
    urllib.request.urlretrieve(url, tmp_path, reporthook=_hook)
    tmp_path.rename(dest_path)
    print(f"\n[AI Enhance] {dest_path.name} ready.")


def ensure_weights():
    """Missing weights ko sirf ek baar auto-download karta hai. Already maujood ho to skip."""
    for fname, url in MODEL_URLS.items():
        dest = WEIGHTS_DIR / fname
        if not dest.exists() or dest.stat().st_size < 1_000_000:
            _download_with_progress(url, dest)


def _load_models():
    """Models sirf ek baar load hote hain (memory mein rehte hain, har frame pe nahi)."""
    global _face_enhancer, _bg_upsampler
    if _face_enhancer is not None:
        return

    ensure_weights()

    from gfpgan import GFPGANer
    from realesrgan import RealESRGANer
    from basicsr.archs.rrdbnet_arch import RRDBNet

    model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64,
                     num_block=23, num_grow_ch=32, scale=2)
    _bg_upsampler = RealESRGANer(
        scale=2,
        model_path=str(WEIGHTS_DIR / "RealESRGAN_x2plus.pth"),
        model=model,
        tile=400,
        tile_pad=10,
        half=True,
    )
    _face_enhancer = GFPGANer(
        model_path=str(WEIGHTS_DIR / "GFPGANv1.4.pth"),
        upscale=2,
        arch="clean",
        channel_multiplier=2,
        bg_upsampler=_bg_upsampler,
    )
    print("[AI Enhance] Models loaded and warm.")


def preload_ai_models():
    """Server boot pe ek hi baar chalta hai — koi user is wait ka intezaar nahi karta."""
    try:
        _load_models()
    except Exception as e:
        print(f"[AI Enhance] Preload failed, will retry on first use: {e}")


def enhance_frame(frame_bgr: np.ndarray) -> np.ndarray:
    """Ek single frame (numpy BGR image) leke enhanced version return karta hai."""
    _load_models()
    _, _, restored = _face_enhancer.enhance(
        frame_bgr,
        has_aligned=False,
        only_center_face=False,
        paste_back=True,
    )
    return restored


def ai_enhance_video(input_path, output_path, ffmpeg_bin, fps=30, progress_cb=None):
    """Poori video ko frame-by-frame AI-enhance karke wapas jodta hai.
    progress_cb(percent, stage) — live progress dikhane ke liye, optional."""
    import subprocess, tempfile, shutil

    tmp_frames = tempfile.mkdtemp()
    tmp_out = tempfile.mkdtemp()

    if progress_cb:
        progress_cb(2, "Extracting frames...")
    subprocess.run([ffmpeg_bin, "-i", str(input_path), f"{tmp_frames}/f_%06d.png"],
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    frames = sorted(os.listdir(tmp_frames))
    total = len(frames) or 1

    for i, fname in enumerate(frames):
        img = cv2.imread(f"{tmp_frames}/{fname}")
        enhanced = enhance_frame(img)
        cv2.imwrite(f"{tmp_out}/f_{i:06d}.png", enhanced)
        if progress_cb:
            pct = 5 + int((i / total) * 90)
            progress_cb(pct, f"Enhancing frame {i+1}/{total}...")

    if progress_cb:
        progress_cb(96, "Re-encoding final video...")
    subprocess.run([
        ffmpeg_bin, "-y", "-framerate", str(fps), "-i", f"{tmp_out}/f_%06d.png",
        "-i", str(input_path), "-map", "0:v", "-map", "1:a",
        "-c:v", "libx264", "-preset", "medium", "-crf", "16",
        "-c:a", "copy", "-pix_fmt", "yuv420p", str(output_path)
    ])

    shutil.rmtree(tmp_frames, ignore_errors=True)
    shutil.rmtree(tmp_out, ignore_errors=True)
    if progress_cb:
        progress_cb(100, "Done")
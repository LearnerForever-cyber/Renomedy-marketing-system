#!/usr/bin/env python3
"""Render deterministic, editable-by-code Instagram PNG assets from a Renomedy content record.

This is the first-party templated renderer: no external image API is required. It creates
real PNG files for feed/carousel/story/reel-cover formats. Reel MP4 rendering is deliberately
not claimed; a Reel remains incomplete until a human supplies the video file.
"""
import argparse
import json
import re
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("ERROR: Pillow is required. Install requirements.txt.", file=sys.stderr)
    raise

ROOT = Path(__file__).resolve().parents[1]
PALETTE = {
    "bg": "#F7F5EC", "ink": "#24443B", "sage": "#667C6B",
    "clay": "#C77952", "sand": "#E8D0A7", "pale": "#E9EEE5",
    "white": "#FFFEF9", "muted": "#64746A", "line": "#D9DED4"
}
W, H = 1080, 1350
STORY_W, STORY_H = 1080, 1920


def safe_slug(value):
    return re.sub(r"[^a-z0-9]+", "-", str(value).lower()).strip("-")[:64] or "post"


def get_font(size, bold=False, serif=False):
    candidates = []
    if serif:
        candidates += ["/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"]
    candidates += ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else
                   "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def wrap_text(draw, text, font, max_width):
    lines, current = [], ""
    for word in str(text).split():
        trial = word if not current else current + " " + word
        if draw.textbbox((0, 0), trial, font=font)[2] <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines or [""]


def draw_block(draw, text, xy, font, fill, max_width, gap=12):
    x, y = xy
    for line in wrap_text(draw, text, font, max_width):
        draw.text((x, y), line, font=font, fill=fill)
        y += draw.textbbox((0, 0), line, font=font)[3] + gap
    return y


def draw_mark(draw, x, y, scale=0.7):
    # Provisional original companion mark, intentionally not represented as an approved logo.
    p = PALETTE
    draw.ellipse((x-58*scale, y-38*scale, x+58*scale, y+78*scale), fill=p["sand"])
    draw.ellipse((x-70*scale, y-55*scale, x+8*scale, y+42*scale), fill=p["sage"])
    draw.ellipse((x-7*scale, y-39*scale, x+66*scale, y+49*scale), fill=p["clay"])
    draw.ellipse((x-20*scale, y-15*scale, x+37*scale, y+47*scale), fill=p["white"])
    draw.ellipse((x-8*scale, y+4*scale, x+1*scale, y+17*scale), fill=p["ink"])
    draw.ellipse((x+17*scale, y+4*scale, x+26*scale, y+17*scale), fill=p["ink"])


def make_canvas(size=(W, H), page=None, total=None):
    p = PALETTE
    im = Image.new("RGB", size, p["bg"])
    d = ImageDraw.Draw(im)
    w, h = size
    d.ellipse((w-230, -130, w+100, 210), fill=p["pale"])
    d.ellipse((-150, h-170, 150, h+130), fill=p["pale"])
    d.text((65, 48), "RENOMEDY  •  FAMILY CARE", font=get_font(22, True), fill=p["sage"])
    d.line((65, 100, w-65, 100), fill=p["line"], width=2)
    if page is not None:
        d.text((w-150, 48), f"{page:02d}/{total:02d}", font=get_font(21, True), fill=p["ink"])
    d.text((65, h-55), "Clearer information. More coordinated care.", font=get_font(19), fill=p["muted"])
    d.text((w-250, h-55), "RENOMEDY", font=get_font(19, True), fill=p["ink"])
    return im, d


def render_card(title, body, path, page=None, total=None, story=False, tag=None):
    size = (STORY_W, STORY_H) if story else (W, H)
    im, d = make_canvas(size, page, total)
    p = PALETTE
    width, height = size
    y = 175 if not story else 270
    if tag:
        d.rounded_rectangle((65, y, 340, y+48), radius=20, fill=p["clay"] if page == 1 else p["sage"])
        d.text((84, y+12), str(tag).upper()[:24], font=get_font(17, True), fill=p["white"])
        y += 100
    elif not story:
        y += 45
    title_size = 56 if not story else 60
    y = draw_block(d, title, (65, y), get_font(title_size, True, True), p["ink"], width-130, 12) + 38
    body_size = 30 if not story else 35
    draw_block(d, body, (65, y), get_font(body_size), p["ink"], width-150, 14)
    if story:
        d.rounded_rectangle((65, height-360, width-65, height-220), radius=28, fill=p["white"], outline=p["line"], width=2)
        d.text((100, height-305), "Add Instagram's native poll sticker if needed", font=get_font(23, True), fill=p["ink"])
    else:
        draw_mark(d, width-190, height-290, .7)
    im.save(path, format="PNG", optimize=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", help="Content JSON record (draft or reviewed record)")
    parser.add_argument("--output-root", default="content/assets")
    args = parser.parse_args()
    try:
        record = json.loads(Path(args.record).read_text(encoding="utf-8"))
        if not isinstance(record, dict) or not isinstance(record.get("creative"), dict):
            raise ValueError("Record must be a JSON object containing a creative object.")
        fmt = record.get("format")
        if fmt not in {"carousel", "reel", "story", "founder_post"}:
            raise ValueError("Unsupported format: " + str(fmt))
        creative = record["creative"]
        title = str(record.get("working_title") or creative.get("hook") or "Renomedy")
        outdir = Path(args.output_root) / safe_slug(record.get("id", title))
        if outdir.exists() and any(outdir.iterdir()):
            raise FileExistsError(f"Asset directory already exists: {outdir}. Choose --output-root or remove it.")
        outdir.mkdir(parents=True, exist_ok=True)
        manifest = {
            "content_id": record.get("id"), "format": fmt, "assets": [],
            "status": "assets_generated", "human_approved": False,
            "brand_note": "Provisional palette and placeholder mark; verify against approved brand assets.",
            "video_note": "PNG cover/script are not a finished Reel video." if fmt == "reel" else None
        }
        if fmt == "carousel":
            slides = [str(x) for x in creative.get("body", []) if str(x).strip()]
            if len(slides) < 2:
                raise ValueError("Carousel needs at least 2 non-empty creative.body slide entries.")
            for i, text in enumerate(slides, 1):
                path = outdir / f"slide-{i:02d}.png"
                # Use first slide as a title-led cover; remaining slides use the supplied text.
                render_card(title if i == 1 else text, text if i == 1 else "Key point: " + text,
                            path, i, len(slides), tag="SAVE THIS" if i == 1 else "RENOMEDY")
                manifest["assets"].append({"path": str(path), "type": "carousel_slide", "index": i})
        elif fmt == "story":
            frames = [str(x) for x in creative.get("story_frames", []) if str(x).strip()]
            if len(frames) < 1:
                raise ValueError("Story needs at least 1 non-empty creative.story_frames entry.")
            for i, text in enumerate(frames, 1):
                path = outdir / f"story-{i:02d}.png"
                render_card(title if i == 1 else "One more thing", text, path, i, len(frames), story=True)
                manifest["assets"].append({"path": str(path), "type": "story_frame", "index": i})
        elif fmt in {"reel", "founder_post"}:
            body = creative.get("reel_script") if fmt == "reel" else "\n".join(creative.get("body", []))
            if fmt == "founder_post" and not body.strip():
                body = creative.get("caption", "")
            if not str(body).strip():
                raise ValueError(f"{fmt} needs a non-empty script/body before assets can be generated.")
            cover = outdir / "cover.png"
            render_card(title, creative.get("cover_text") or creative.get("hook") or title, cover)
            manifest["assets"].append({"path": str(cover), "type": "reel_cover" if fmt == "reel" else "feed_graphic"})
            text_path = outdir / ("reel-script.txt" if fmt == "reel" else "founder-outline.txt")
            text_path.write_text(str(body).strip() + "\n", encoding="utf-8")
            manifest["assets"].append({"path": str(text_path), "type": "video_script" if fmt == "reel" else "post_outline"})
            manifest["status"] = "assets_generated_video_incomplete" if fmt == "reel" else "assets_generated"
        manifest_path = outdir / "asset-manifest.json"
        manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(json.dumps({"output_dir": str(outdir), "asset_count": len(manifest["assets"]), "status": manifest["status"], "manifest": str(manifest_path)}, indent=2))
        if fmt == "reel":
            print("NOTE: Reel assets are not complete until a rendered MP4 is supplied and checked.")
        print("Human approval remains required. Asset generation does not publish.")
        return 0
    except (OSError, json.JSONDecodeError, ValueError, FileExistsError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Check a 16:9 landscape master against 4:3 / 3:4 / 9:16 / 1:1 center crops.

Usage:
  python3 safe_zone_check.py master.mp4 boxes.json [--frames OUTDIR] [--offset X:Y ...]
boxes.json: [{"name": "subtitle", "x": 360, "y": 940, "w": 1200, "h": 100}, ...]
            coordinates in master pixels.
Needs ffprobe (and ffmpeg for --frames). Python standard library otherwise.

For every target ratio it computes the largest crop of that ratio, centred
(or shifted with --offset 3:4=+200), reports which boxes are fully inside,
prints the FFmpeg crop/scale command, and with --frames exports one checked
frame per ratio with the crop drawn, so a human can eyeball it.
"""
import json, os, subprocess, sys
from fractions import Fraction

TARGETS = {"4:3": (1440, 1080), "3:4": (1080, 1440), "9:16": (1080, 1920), "1:1": (1080, 1080)}
MARGIN = 0.05  # keep text 5% away from crop edges (platform UI)

def probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                          "-show_entries", "stream=width,height,duration",
                          "-of", "json", path], capture_output=True, text=True, check=True)
    s = json.loads(out.stdout)["streams"][0]
    return int(s["width"]), int(s["height"]), float(s.get("duration", 0) or 0)

def crop_rect(W, H, ratio, dx=0):
    rw, rh = map(int, ratio.split(":"))
    if Fraction(W, H) > Fraction(rw, rh):
        h = H; w = (H * rw // rh) // 2 * 2
    else:
        w = W; h = (W * rh // rw) // 2 * 2
    x = max(0, min(W - w, (W - w) // 2 + dx)); y = (H - h) // 2
    return x, y, w, h

def inside(b, r):
    x, y, w, h = r
    mx, my = w * MARGIN, h * MARGIN
    return (b["x"] >= x + mx and b["y"] >= y + my and
            b["x"] + b["w"] <= x + w - mx and b["y"] + b["h"] <= y + h - my)

def main(argv):
    master, boxes_path = argv[1], argv[2]
    frames = argv[argv.index("--frames") + 1] if "--frames" in argv else None
    offsets = {}
    for i, a in enumerate(argv):
        if a == "--offset":
            k, v = argv[i + 1].split("=")
            offsets[k] = int(v)
    W, H, dur = probe(master)
    boxes = json.load(open(boxes_path, encoding="utf-8"))
    print(f"母版 {W}×{H}，时长 {dur:.1f}s")
    fails = 0
    if Fraction(W, H) != Fraction(16, 9):
        print("ERROR 母版不是 16:9"); fails += 1
    for ratio, (tw, th) in TARGETS.items():
        r = crop_rect(W, H, ratio, offsets.get(ratio, 0))
        bad = [b["name"] for b in boxes if not inside(b, r)]
        status = "OK  " if not bad else "FAIL"
        fails += bool(bad)
        print(f"{status} {ratio:<5} 裁切 x={r[0]} y={r[1]} {r[2]}×{r[3]}  "
              + ("全部在安全区" if not bad else "出界: " + ", ".join(bad)))
        print(f"      ffmpeg -i in.mp4 -vf \"crop={r[2]}:{r[3]}:{r[0]}:{r[1]},scale={tw}:{th}\" -c:a copy out_{ratio.replace(':','x')}.mp4")
        if frames:
            os.makedirs(frames, exist_ok=True)
            draw = ",".join(f"drawbox=x={b['x']}:y={b['y']}:w={b['w']}:h={b['h']}:color=red@0.8:t=4" for b in boxes)
            vf = f"{draw},drawbox=x={r[0]}:y={r[1]}:w={r[2]}:h={r[3]}:color=lime:t=6"
            out = os.path.join(frames, f"check_{ratio.replace(':','x')}.png")
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(min(1, dur / 2)), "-i", master,
                            "-frames:v", "1", "-vf", vf, out], check=True)
            print(f"      检查帧: {out}")
    print("结论: " + ("所有比例通过" if not fails else f"{fails} 项不通过，按 references/fixes.md 补救"))
    return 1 if fails else 0

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(2)
    sys.exit(main(sys.argv))

#!/usr/bin/env python3
"""Check cover PNG size/ratio and that text boxes sit inside the safe zone.

Usage: python3 check_cover.py cover.png [boxes.json]
boxes.json: [{"name": "title", "x": 300, "y": 400, "w": 800, "h": 200}, ...]
Pure standard library (reads the PNG IHDR header only).
Safe zones (from SKILL.md): vertical 3:4 text y in 280–1640 of a 1920 tall
reference -> scaled to image height; horizontal 4:3 text x in 260–1660 of a
1920 wide reference -> scaled to image width. Title height ≥14% on 3:4.
"""
import json, struct, sys

TARGETS = {"4:3": (1440, 1080), "3:4": (1080, 1440), "1:1": (1080, 1080)}

def png_size(path):
    with open(path, "rb") as f:
        head = f.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("不是 PNG 文件")
    return struct.unpack(">II", head[16:24])

def main(argv):
    w, h = png_size(argv[1])
    ratio = next((k for k, (tw, th) in TARGETS.items() if w * th == h * tw), None)
    err = 0
    print(f"尺寸 {w}×{h}，比例 {ratio or '不符合 4:3 / 3:4 / 1:1'}")
    if ratio is None:
        err += 1
    elif (w, h) != TARGETS[ratio]:
        print(f"WARN  比例对，但建议导出为 {TARGETS[ratio][0]}×{TARGETS[ratio][1]}")
    if len(argv) > 2 and ratio:
        boxes = json.load(open(argv[2], encoding="utf-8"))
        for b in boxes:
            x0, y0, x1, y1 = b["x"], b["y"], b["x"] + b["w"], b["y"] + b["h"]
            if ratio == "3:4":
                lo, hi = 280 / 1920 * h, 1640 / 1920 * h
                ok = lo <= y0 and y1 <= hi
                zone = f"y {lo:.0f}–{hi:.0f}"
                if b.get("name") == "title" and b["h"] / h < 0.14:
                    print(f"ERROR {b['name']}: 字高 {b['h']/h:.0%} < 14%"); err += 1
            else:
                lo, hi = 260 / 1920 * w, 1660 / 1920 * w
                ok = lo <= x0 and x1 <= hi
                zone = f"x {lo:.0f}–{hi:.0f}"
            if not (0 <= x0 and 0 <= y0 and x1 <= w and y1 <= h):
                print(f"ERROR {b['name']}: 超出画面"); err += 1
            elif not ok:
                print(f"ERROR {b['name']}: 出了安全区（{zone}）"); err += 1
            else:
                print(f"OK    {b['name']}: 在安全区内（{zone}）")
    print("结论: " + ("通过" if err == 0 else f"{err} 个问题，重做"))
    return 1 if err else 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    sys.exit(main(sys.argv))

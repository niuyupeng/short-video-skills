#!/usr/bin/env python3
"""Lint a cross-post draft folder (bili.txt / xhs.txt / sph.txt).

Usage: python3 check_crosspost.py <folder>
Each file uses `键: 值` lines, e.g. `标题: ...`, `标签: a,b,c`, `AI标识: 是`.
Checks: STATUS DRAFT present; title length per platform; tag counts;
AI disclosure = 是; no mention of other platforms or 引流 words.
"""
import os, re, sys

LIMITS = {"bili.txt": ("B站", 80, (1, 10)), "xhs.txt": ("小红书", 20, (5, 8)), "sph.txt": ("视频号", 30, (3, 5))}
OTHER = {"bili.txt": r"抖音|小红书|视频号", "xhs.txt": r"抖音|B站|b站|视频号", "sph.txt": r"抖音|B站|b站|小红书"}
LURE = re.compile(r"加微信|vx|私信领取|点赞过|关注领取|wx", re.I)

def fields(path):
    d = {}
    for line in open(path, encoding="utf-8"):
        if ":" in line or "：" in line:
            k, v = re.split(r"[:：]", line, maxsplit=1)
            d[k.strip()] = v.strip()
    return d, open(path, encoding="utf-8").read()

def main(folder):
    err = 0
    status = os.path.join(folder, "STATUS")
    if not (os.path.exists(status) and "DRAFT" in open(status, encoding="utf-8").read()):
        print("ERROR 没有 STATUS: DRAFT 文件"); err += 1
    for fn, (plat, tmax, (tmin_tags, tmax_tags)) in LIMITS.items():
        p = os.path.join(folder, fn)
        if not os.path.exists(p):
            print(f"SKIP  {plat}: 无 {fn}"); continue
        d, text = fields(p)
        title = d.get("标题", "")
        tags = [t for t in re.split(r"[,，\s#]+", d.get("标签", d.get("话题", ""))) if t]
        checks = [
            (0 < len(title) <= tmax, f"标题 {len(title)} 字（上限 {tmax}）"),
            (tmin_tags <= len(tags) <= tmax_tags, f"标签 {len(tags)} 个（应 {tmin_tags}–{tmax_tags}）"),
            (d.get("AI标识") == "是", "AI标识为「是」"),
            (not re.search(OTHER[fn], text), "不提其他平台"),
            (not LURE.search(text), "无引流/诱导词"),
        ]
        for ok, msg in checks:
            print(("OK    " if ok else "ERROR ") + f"{plat}: {msg}")
            err += 0 if ok else 1
    print(f"错误 {err} 个")
    return 1 if err else 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__); sys.exit(2)
    sys.exit(main(sys.argv[1]))

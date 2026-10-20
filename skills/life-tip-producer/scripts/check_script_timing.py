#!/usr/bin/env python3
"""Check a timecoded life-tip script against the 35–55s template.

Usage: python3 check_script_timing.py SCRIPT.txt [--min 35 --max 55]
Lines look like: `0–3s 钩子: 口播文字` (– or - both fine).
Checks: total length in range; first segment starts at 0 and hook ≤18 字;
no gaps/overlaps; speaking rate 3–6 字/秒 per segment; has a 来源/出处 mention.
"""
import re, sys

SEG = re.compile(r"^\s*(\d+(?:\.\d+)?)\s*[–\-~]\s*(\d+(?:\.\d+)?)\s*s\s*([^:：]*)[:：]\s*(.*)$")
HAN = re.compile(r"[\u4e00-\u9fff]")

def main(argv):
    path = argv[1]
    lo = float(argv[argv.index("--min") + 1]) if "--min" in argv else 35
    hi = float(argv[argv.index("--max") + 1]) if "--max" in argv else 55
    segs = [m.groups() for m in map(SEG.match, open(path, encoding="utf-8")) if m]
    err = 0
    if not segs:
        print("ERROR 没有找到时间码段落"); return 1
    prev = 0.0
    for i, (a, b, label, text) in enumerate(segs):
        a, b = float(a), float(b)
        n = len(HAN.findall(text)); dur = b - a
        rate = n / dur if dur > 0 else 0
        if abs(a - prev) > 0.01:
            print(f"ERROR {a:g}s: 与上一段不衔接（上一段止于 {prev:g}s）"); err += 1
        flag = "" if 3 <= rate <= 6 else "  ← 语速异常"
        if flag: err += 1
        print(f"{a:>5g}–{b:<5g}s {label.strip():<8} {n:>3} 字  {rate:.1f} 字/秒{flag}")
        if i == 0 and (a != 0 or n > 18):
            print("ERROR 钩子必须从 0 秒开始且 ≤18 字"); err += 1
        prev = b
    if not lo <= prev <= hi:
        print(f"ERROR 总时长 {prev:g}s，不在 {lo:g}–{hi:g}s"); err += 1
    if not re.search(r"出处|来源|研究|指南", open(path, encoding="utf-8").read()):
        print("ERROR 没有标注出处"); err += 1
    print(f"总时长 {prev:g}s，问题 {err} 个")
    return 1 if err else 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    sys.exit(main(sys.argv))

#!/usr/bin/env python3
"""Validate an A/B win log (Markdown table) and title variants.

Usage: python3 check_win_log.py WIN_LOG.md
Columns: 日期 | 片名 | 元素 | 版本A | 版本B | 平台 | 指标 | 赢家 | 数据来源 | 学到
Rules: 赢家 must be A/B/C/平/待定; a winner needs a real 指标 and 数据来源
(指标=待数据 -> 赢家 must be 待定); 元素=标题 -> each version ≤ 30 字 and
no unsourced absolute words (最/第一/治愈/根治).
"""
import re, sys

ABSOLUTE = re.compile(r"最|第一|治愈|根治|100%")

def rows_of(text):
    rows = [l.strip() for l in text.splitlines() if l.strip().startswith("|")]
    rows = [r for r in rows if not re.fullmatch(r"\|[\s:\-|]+\|", r)]
    return [[c.strip() for c in r.strip("|").split("|")] for r in rows]

def main(path):
    rows = rows_of(open(path, encoding="utf-8").read())
    if not rows:
        print("ERROR 没有表格"); return 1
    h, body = rows[0], rows[1:]
    need = ["日期", "片名", "元素", "版本A", "版本B", "指标", "赢家", "数据来源"]
    miss = [c for c in need if c not in h]
    if miss:
        print("ERROR 缺少列: " + ",".join(miss)); return 1
    g = lambda r, c: r[h.index(c)] if h.index(c) < len(r) else ""
    err = 0
    for r in body:
        tag = f"{g(r,'日期')} {g(r,'片名')} {g(r,'元素')}"
        win, metric, src = g(r, "赢家"), g(r, "指标"), g(r, "数据来源")
        if win not in {"A", "B", "C", "平", "待定"}:
            print(f"ERROR {tag}: 赢家只能是 A/B/C/平/待定，现在是「{win}」"); err += 1
        if win in {"A", "B", "C"} and (metric in ("", "待数据") or not src):
            print(f"ERROR {tag}: 判了赢家但没有真实指标或数据来源"); err += 1
        if g(r, "元素") == "标题":
            for v in ("版本A", "版本B"):
                t = g(r, v)
                if len(t) > 30:
                    print(f"WARN  {tag}: {v} {len(t)} 字，超过 30"); 
                if ABSOLUTE.search(t):
                    print(f"WARN  {tag}: {v} 含绝对化用词，需审核放行"); 
    print(f"共 {len(body)} 条，错误 {err} 个")
    return 1 if err else 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__); sys.exit(2)
    sys.exit(main(sys.argv[1]))

#!/usr/bin/env python3
"""Validate a fact ledger (Markdown table) before a PASS verdict.

Usage: python3 check_fact_ledger.py LEDGER.md
Expected header columns (order free): # | 原句 | 类型 | 一手来源 | 来源原话 | 结论
Exit code 0 = no blocking problem, 1 = problems found.
"""
import re, sys

REQUIRED = ["#", "原句", "类型", "一手来源", "来源原话", "结论"]
VERDICTS = {"OK", "改", "删"}
SECONDARY = re.compile(r"百科|wiki|知乎|公众号|自媒体|新闻|baike", re.I)
PRIMARY_HINT = re.compile(r"doi|10\.\d{4,}/|官方|原著|卷|页|pp\.|isbn|指南|guideline|http", re.I)

def parse_table(text):
    rows = [l.strip() for l in text.splitlines() if l.strip().startswith("|")]
    rows = [r for r in rows if not re.fullmatch(r"\|[\s:\-|]+\|", r)]
    if not rows:
        return None, []
    cells = lambda r: [c.strip() for c in r.strip("|").split("|")]
    return cells(rows[0]), [cells(r) for r in rows[1:]]

def main(path):
    header, rows = parse_table(open(path, encoding="utf-8").read())
    if header is None:
        print("ERROR 没有找到表格"); return 1
    missing = [c for c in REQUIRED if c not in header]
    if missing:
        print("ERROR 缺少列: " + ", ".join(missing)); return 1
    idx = {c: header.index(c) for c in REQUIRED}
    problems = 0
    for r in rows:
        r += [""] * (len(header) - len(r))
        get = lambda c: r[idx[c]]
        n, verdict, src, quote = get("#"), get("结论"), get("一手来源"), get("来源原话")
        if verdict not in VERDICTS:
            print(f"ERROR 第{n}条 结论必须是 OK/改/删，现在是「{verdict}」"); problems += 1
        if verdict == "OK":
            if not src:
                print(f"ERROR 第{n}条 结论 OK 但没有一手来源"); problems += 1
            elif SECONDARY.search(src) and not PRIMARY_HINT.search(src):
                print(f"ERROR 第{n}条 来源像二手资料（{src}），只能当线索"); problems += 1
            if not quote:
                print(f"ERROR 第{n}条 结论 OK 但没有摘来源原话"); problems += 1
    print(f"共 {len(rows)} 条，问题 {problems} 个 → " + ("可以进入结论" if problems == 0 else "不能给 PASS"))
    return 1 if problems else 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__); sys.exit(2)
    sys.exit(main(sys.argv[1]))

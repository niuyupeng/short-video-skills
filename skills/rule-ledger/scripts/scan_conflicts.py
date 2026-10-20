#!/usr/bin/env python3
"""Scan a dated rule ledger for conflicts, then find stale values in skill files.

Usage: python3 scan_conflicts.py RULES.md [SKILLS_DIR] [--patch OUT.md]
RULES.md table columns: id | 生效日期 | 键 | 值 | 来源 | 旧值写法(可选)
  - same 键 with different 值: latest 生效日期 wins, older rows become 已废止
  - same 键 and same date but different 值: real conflict, needs a human
  - 旧值写法: comma-separated strings that indicate the old value in prose
    (e.g. "9:16,竖版"); the scanner greps SKILLS_DIR for them.
Standard library only. Read-only: --patch writes a patch *draft*, never edits skills.
"""
import os, re, sys
from collections import defaultdict
from datetime import date

def rows_of(text):
    rows = [l.strip() for l in text.splitlines() if l.strip().startswith("|")]
    rows = [r for r in rows if not re.fullmatch(r"\|[\s:\-|]+\|", r)]
    return [[c.strip() for c in r.strip("|").split("|")] for r in rows]

def main(argv):
    rows = rows_of(open(argv[1], encoding="utf-8").read())
    h, body = rows[0], rows[1:]
    col = {c: h.index(c) for c in h}
    g = lambda r, c: r[col[c]] if c in col and col[c] < len(r) else ""
    by_key = defaultdict(list)
    for r in body:
        by_key[g(r, "键")].append(r)
    live, superseded, conflicts = {}, [], []
    for k, rs in by_key.items():
        rs.sort(key=lambda r: date.fromisoformat(g(r, "生效日期")))
        top = date.fromisoformat(g(rs[-1], "生效日期"))
        tops = {g(r, "值") for r in rs if date.fromisoformat(g(r, "生效日期")) == top}
        if len(tops) > 1:
            conflicts.append((k, top, tops))
            continue  # no winner until a human decides
        live[k] = rs[-1]
        superseded += [(k, r, rs[-1]) for r in rs[:-1] if g(r, "值") != g(rs[-1], "值")]
    print(f"规则 {len(body)} 条，键 {len(by_key)} 个")
    for k, d, vals in conflicts:
        print(f"CONFLICT {k}: {d} 同一天有 {len(vals)} 个值 {sorted(vals)} → 必须人工裁定")
    for k, old, new in superseded:
        print(f"SUPERSEDED {g(old,'id')} {k}={g(old,'值')}（{g(old,'生效日期')}）→ 以 {g(new,'id')} {g(new,'值')}（{g(new,'生效日期')}）为准")
    hits = []
    if len(argv) > 2 and not argv[2].startswith("--"):
        for k, old, new in superseded:
            needles = [s.strip() for s in g(old, "旧值写法").split(",") if s.strip()] or [g(old, "值")]
            for root, _, files in os.walk(argv[2]):
                for fn in files:
                    if not fn.endswith((".md", ".txt", ".json", ".py")):
                        continue
                    p = os.path.join(root, fn)
                    for n, line in enumerate(open(p, encoding="utf-8", errors="ignore"), 1):
                        if any(s in line for s in needles) and g(new, "值") not in line and "~~" not in line:
                            hits.append((p, n, line.strip(), k, new))
        for p, n, line, k, new in hits:
            print(f"STALE {os.path.relpath(p, argv[2])}:{n} [{k}] 「{line[:60]}」 应为 {g(new,'值')}（{g(new,'id')}）")
    if "--patch" in argv:
        out = argv[argv.index("--patch") + 1]
        with open(out, "w", encoding="utf-8") as f:
            f.write("# 规则补丁草稿（未修改任何文件，需人工确认）\n\n")
            for p, n, line, k, new in hits:
                f.write(f"- `{os.path.relpath(p, argv[2])}` 第 {n} 行 [{k}]\n  - 现在: {line}\n  - 建议: 改为 {g(new,'值')}，旧写法用删除线保留，注明 {g(new,'id')} {g(new,'生效日期')}\n")
        print(f"补丁草稿: {out}")
    print(f"冲突 {len(conflicts)}，已废止 {len(superseded)}，残留旧值 {len(hits)}")
    return 1 if conflicts or hits else 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    sys.exit(main(sys.argv))

#!/usr/bin/env python3
"""Check a per-post metrics CSV: every number needs a source and capture time.

Usage: python3 check_metrics.py metrics.csv
Columns: 片名,播放,完播率,3s留存,涨粉,来源截图,采集时间  (extra columns allowed)
Rules: a filled metric with empty 来源截图 or 采集时间 is an error;
       播放 < 1000 -> 「样本太小，不下结论」; empty metric must be written 无数据.
"""
import csv, sys

METRICS = ["播放", "完播率", "3s留存", "涨粉"]

def main(path):
    errors = 0
    with open(path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    for i, r in enumerate(rows, 2):
        name = r.get("片名", f"第{i}行")
        filled = [m for m in METRICS if (r.get(m) or "").strip() not in ("", "无数据")]
        blank = [m for m in METRICS if (r.get(m) or "").strip() == ""]
        if blank:
            print(f"ERROR {name}: {','.join(blank)} 为空，没有数据请写「无数据」"); errors += 1
        if filled and not (r.get("来源截图") or "").strip():
            print(f"ERROR {name}: 有数字但没有来源截图"); errors += 1
        if filled and not (r.get("采集时间") or "").strip():
            print(f"ERROR {name}: 有数字但没有采集时间"); errors += 1
        plays = (r.get("播放") or "").replace(",", "").strip()
        if plays.isdigit() and int(plays) < 1000:
            print(f"NOTE  {name}: 播放 {plays} < 1000，样本太小，不下结论")
    print(f"共 {len(rows)} 条，错误 {errors} 个")
    return 1 if errors else 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__); sys.exit(2)
    sys.exit(main(sys.argv[1]))

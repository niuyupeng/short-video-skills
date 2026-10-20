---
name: content-data-review
description: >-
  Use when reviewing a short video's performance (完播率, 3s retention, follower
  gain), running the weekly 对标 account teardown, or turning performance findings
  into topic/hook/packaging recommendations — never invents numbers.
---
# Content data review (数据复盘)

Hard rules
- Never estimate, round up, or fabricate a metric. If a number is not in a screenshot/export 负责人 gave, or a page you actually read, write「无数据」and ask 负责人 for a screenshot of the creator backend (作品分析页: 播放、完播率、2s/3s/5s跳出、平均播放时长、涨粉、互动).
- Every number carries its source and capture time (负责人所在时区).
- 外部无许可证内容（对标号文案、画面）只学思路，不抄内容。
- Read-only on platforms. No login automation, no paid scrapers, no crawler QR logins.

## 1. Per-post review (48h and 7d)
| 日期 | 账号 | 片名 | 时长 | 播放 | 完播率 | 3s留存 | 均播时长/时长 | 点赞 | 评论 | 转发 | 收藏 | 涨粉 | 粉转率 | 来源截图 |
Diagnose in order (first failing stage is the bottleneck):
1. 3s留存 low → hook/cover/first frame → hand to 包装.
2. 3s ok, 完播 low → name the drop second and the line/visual there.
3. 完播 ok, interaction low → ending lacks dilemma/question/shareable line.
4. Interaction ok, 涨粉 low → account promise unclear.
Compare only against the same account's median of last 10 posts.

## 2. Weekly 对标 teardown
每周 3–5 个对标号、各取 3 条公开爆款，逐条拆钩子/节拍/包装，产出 5 条可借鉴清单。
详见 [references/weekly-teardown.md](references/weekly-teardown.md)。

## 3. Feedback memo (weekly, to content lead + growth lead)
```
本周结论（≤5条：现象 → 证据(数字+来源) → 建议动作 → 负责人）
赢的标题/封面/开头 (from 包装 win log)
下周选题加权
缺数据: 需要负责人截图的作品列表
```

## 4. Hygiene
- <1k plays: 「样本太小，不下结论」.
- Separate correlation from cause; one change per A/B.

## 常见错误
- 把「看起来大概」写成数字：没有截图就写「无数据」。
- 跨账号比：只和本账号最近 10 条的中位数比。
- 一条播放不到 1000 就下结论。
- 一次 A/B 同时改两处，然后把结果归给其中一处。
- 把相关当因果：「发布时间改了，播放涨了」不等于时间起作用。

## 输出模板
```
片名 / 时长 / 采集时间（时区）/ 来源截图
| 指标 | 数值 | 本号近10条中位数 | 判断 |
瓶颈环节: 3s留存 | 完播 | 互动 | 涨粉
掉点: 第 X 秒「原句/画面」
建议动作（≤3 条）→ 交给谁
缺数据: …
```

## 工具
`scripts/check_metrics.py metrics.csv`：每个数字必须带来源截图和采集时间，空值必须写「无数据」，播放 <1000 提示样本太小。

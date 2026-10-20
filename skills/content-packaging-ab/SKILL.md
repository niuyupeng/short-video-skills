---
name: content-packaging-ab
description: Use when a short video needs title, cover (4:3 / 3:4) or first-3-second hook variants for A/B testing, or when recording which packaging version won.
---
# Content packaging A/B (标题 · 封面 · 开头3秒)

Inputs: final script, account positioning, platform list, prior win log.
For cover visual craft, run @cover-top-tier first; this skill adds variants and testing.

## 1. Titles — write 3, each a different lever
- A 反常识: 「X其实不是Y」
- B 具体场景/痛点: 你在什么时候遇到什么
- C 数字/出处: 「具体数字或年份｜出处名」
Checks: matches content (no 标题党), key word in first 8 字, no effect/technique jargon, platform length limits, no banned/absolute words (最/第一/治愈) unless sourced and cleared by 审核.

## 2. Covers — 2–3 variants per ratio
- Sizes: 横 4:3 1440×1080 为主，竖 3:4 1080×1440 继续出（抖音主页/推荐页用竖版）; 视频本体一律 16:9 (B站 also 16:9 1920×1080, key text in center 4:3 safe zone).
- One focal object, ≤10 large 字 main line, ≤30% text area, high contrast, readable at thumbnail (test at 25% scale).
- Variant axes: object close-up vs. person/emotion vs. big-word typographic. Change one axis per variant.
- Avoid platform UI zones (right-bottom duration, bottom info bar); no other platforms' logos.
- Series consistency: same font family, color band and corner mark per account.

## 3. First-3-second hook — 3 variants
出 3 版，每版含口播（≤18 字）、屏幕字、首帧画面、0–1s 与 1–3s 节拍；首帧必须能当封面。
详见 [references/hook-patterns.md](references/hook-patterns.md)。

## 4. Deliverable
```
PACKAGING_<slug>.md
  标题 A/B/C + 推荐理由
  封面 files: cover_3x4_A.jpg, cover_3x4_B.jpg, cover_4x3_A.jpg ...
  开头 A/B/C 文本 + 首帧描述
  推荐组合 + 测试计划（哪个平台/时段用哪个版本）
```

## 5. Win log (append-only)
| 日期 | 片名 | 元素 | 版本A | 版本B | 平台 | 指标(3s留存/点击) | 赢家 | 数据来源 | 学到 |
Only fill metrics from 数据复盘; otherwise「待数据」. Monthly: distill 3 rules from the log into the account playbook.

## 常见错误
- 一个版本同时改了两个杠杆，赢了也说不清为什么。
- 没有数据就判赢家：指标写「待数据」，赢家写「待定」。
- 标题和内容不符（标题党），或用了没放行的「最/第一/治愈」。
- 首帧当不了封面。
- 封面只出一种比例。

## 输出模板
```
PACKAGING_<slug>.md
| 元素 | A | B | C | 每版只改的那一处 |
推荐组合: … 理由: …
测试计划: 平台 / 时段 / 先测 A 对 ?
WIN_LOG 预登记: 日期 | 片名 | 元素 | 版本A | 版本B | 平台 | 待数据 | 待定 | | |
```

## 工具
`scripts/check_win_log.py WIN_LOG.md`：赢家必须有真实指标和数据来源；标题超长或有绝对化用词时提醒。

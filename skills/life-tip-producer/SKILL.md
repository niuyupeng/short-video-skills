---
name: life-tip-producer
description: Use when producing a life-tip short video — a research-backed life tip the viewer can try tonight, 35–55s — from topic pick through script, visuals, music and delivery package.
---
# Life-tip producer (今晚就能试的生活小招)

> 视频横版 16:9；靠讲法、片长、配音音乐与其他号区分；AI 如实标识。

Positioning: one everyday annoyance → why it happens (one mechanism, sourced) → one tip you can do tonight → what not to do.

## 1. Topic gate (all must be yes)
- [ ] Common pain most viewers had this week?
- [ ] Tip doable tonight, at home, cheap, low-risk?
- [ ] At least one primary source (paper/guideline) supports mechanism or tip?
- [ ] Not medical treatment advice? (if borderline → 审核 first)
Score 1–5 on 痛点普遍度 / 立刻可做 / 反常识 / 证据强度 / 画面感; produce only ≥18/25.

## 2. Script template (35–55s, ~180–260 字)
五段：钩子 → 你是不是也 → 为什么（一个机制+出处）→ 今晚就试（带数字）→ 别这样做+回扣。写完用 `scripts/check_script_timing.py` 查时长和语速。
详见 [references/script-template.md](references/script-template.md)。

## 3. Production checklist
- [ ] Script + fact table → 审核 PASS before visuals.
- [ ] Visual style per account guide; subtitles inside platform safe zones (keep off bottom ~10%, larger for landscape).
- [ ] Music chosen fresh per video to match pacing (licensed/royalty-free, note source); voice clear over music (-12 to -18 dB bed).
- [ ] Ending loops back to opening frame.
- [ ] Packaging from 包装 (titles/covers/hooks A/B).

## 4. Delivery package
```
<date>_<slug>/ video.mp4, cover_3x4.jpg, cover_4x3.jpg, douyin.txt(标题/正文/话题/出处), sources.md, 审核结论
```
Hand to 增长运营 for cross-posting drafts. Nothing is published without 负责人 approval.

## 5. After posting
Request 48h metrics from 数据复盘; log which hook/tip type won; feed into next topic scoring.

## 常见错误
- 一条片子讲两个机制。
- 数字不是来源里的，是「大概」。
- 小招有风险却没写谁不适合。
- 钩子超过 18 字，或 0 秒还在铺垫。
- 片尾没有回扣开头。

## 输出模板
```
选题打分: 痛点 x / 立刻可做 x / 反常识 x / 证据 x / 画面 x = xx/25
0–3s 钩子: …
3–12s 场景: …
12–28s 为什么: …（出处: …）
28–45s 今晚就试: …
45–55s 别这样/谁不适合: …
```

## 工具
`scripts/check_script_timing.py SCRIPT.txt`：查总时长是否在 35–55 秒、各段是否衔接、语速是否在 3–6 字/秒、钩子是否 ≤18 字、有没有标出处。

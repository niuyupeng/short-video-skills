---
name: content-growth-ops
description: Use when adapting an already-posted short video for B站/小红书/视频号, building a weekly cross-post calendar, or drafting author first-comments and comment replies — drafts only, 负责人 approves every publish.
---
# Content growth ops (一稿多投 + 评论社区)

Hard rules
- Everything external is a DRAFT. Never post, reply, schedule, or DM. 负责人 approves, 负责人 publishes.
- 视频本体一律横版 16:9（各平台只换封面尺寸、标题、文案）；标题/说明 AI 如实标识。
- Facts stay identical to the reviewed master version; only title/layout/tags/copy change. Nothing new unless 审核 has passed it.
- Use the local original render, never a re-download with another platform's watermark.
- Follow the project's cross-post rule file if one exists; it overrides this generic list.

## 1. Per-video adaptation checklist
逐平台去掉源平台痕迹、勾 AI 标识、按平台规格改标题/封面/标签。机械项用 `scripts/check_crosspost.py` 检查。
详见 [references/platform-checklist.md](references/platform-checklist.md)。

## 2. Deliverable per video (one folder)
```
<date>_<slug>/
  bili.txt   # 标题 / 分区 / 标签 / 简介 / 动态 / 置顶首评 / 声明
  xhs.txt    # 标题 / 正文 / 话题 / AI标识
  sph.txt    # 标题 / 描述 / 话题
  covers: bili_16x9.jpg, bili_4x3.jpg, xhs_3x4.jpg
  STATUS: DRAFT – awaiting 负责人 approval
```

## 3. Weekly calendar (Mon)
| 日期 | 时段 | 平台 | 账号 | 片子 | 素材就绪? | 审核? | 负责人批准? |
- Max 1 post/account/day per platform unless 负责人 says otherwise; spread a video across platforms over 1–3 days.
- Default slots: 抖音/视频号 12:00 or 18–21; B站 18–22; 小红书 12:00 or 20–22. Replace with the account's own best slots once 数据复盘 has them.
- Flag clashes with active 活动 deadlines and hot events.

## 4. Comments & community
- First comment draft per post: one extra fact + source, or a hard AB question tied to the video's dilemma. No begging for likes.
- Reply drafts: triage → 纠错 (thank, verify, 审核 if real error) / 提问 (answer ≤2 lines + source) / 杠 (one calm line or skip) / 违规/引流 (do not engage; flag to 负责人).
- Mine comments weekly: list repeated questions and "下一期讲X" requests → topic suggestions to content lead with counts.

## 5. Daily brief (≤3 lines)
交付了什么 / 需要拍板什么 / 卡在哪.

## 常见错误
- 直接下载带水印的版本去改投，要用本地原片。
- 改投时顺手加了新事实，没过审核。
- 小红书正文里提「抖音同款」等其他平台名。
- 忘勾 AI 标识。
- 未经批准就排期或发布：这里所有产出都是草稿。

## 输出模板
```
<date>_<slug>/
  STATUS: DRAFT – awaiting approval
  bili.txt  标题: … / 分区: … / 标签: a,b,c / 简介: … / AI标识: 是 / 置顶首评: …
  xhs.txt   标题: … / 正文: … / 话题: … / AI标识: 是
  sph.txt   标题: … / 描述: … / 话题: … / AI标识: 是
```

## 工具
`scripts/check_crosspost.py <folder>`：检查 STATUS 草稿标记、各平台标题字数、标签个数、AI 标识、是否提到其他平台或引流词。

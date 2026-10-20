---
name: cover-top-tier
description: >-
  Use before designing, reviewing, or remaking a short-video knowledge cover
  (Douyin/B站/小红书), or when a cover looks cheap, templated, or like a PPT slide.
---
# 顶尖短视频知识封面

## 画幅
- 视频本体：横版 16:9。
- 封面：横版 4:3 为主；竖版 3:4 继续出（抖音主页和推荐页用竖版）。不得只出横版。
- 合集另出 1080²。

## Hard rules
1. One world — not pure gradient cloth; tactile prop or scene ≥50–70%.
2. Smash title: 2 lines, ≤11 chars total; question / contrast / number hook; one keyword highlight.
3. Type height on 3:4 ≥14% (aim 16–18%); 4:3 同样保证 25% 缩略图可读.
4. Safe zones: vertical text y≈280–1640; horizontal x≈260–1660 (1920 宽基准).
5. No badge pile (gold laurel + avatar certificate kit).
6. No AI garbled glyphs — generate prop/person plate without text, then overlay crisp Chinese with fonts.
7. 出镜人物只用本人授权的参考图（路径在本地配置，不入库）；人物指向题目物件。色调按题目选，不锁定。
8. 账号角标仅放角落；不同账号不互相照搬吉祥物/配色元素。
9. 号与号的区分靠讲法、片长、配音音乐，不靠封面底色撞脸。
10. Deliver only upload-ready 4:3 + 3:4 (+1080² for collection). One final file per slot.

## Fail = redo
Looks like PPT / 电商主图 / 毕业证书 / garbled text / 缺竖版 3:4.

## 常见错误
- 让图像模型直接画中文字。
- 大字超过 11 个，或缩到 25% 读不出。
- 文字压在右下角时长角标或底部信息栏上。
- 用未经授权的真人照片或 AI 生成的真人。
- 只交横版。

## 输出模板
```
| 项 | 横 4:3 1440×1080 | 竖 3:4 1080×1440 |
| 大字（≤11 字，高亮词） | | |
| 主体物件及占比 | | |
| 文字框坐标 | | |
| 25% 缩略图自检 | | |
交付: cover_4x3.png, cover_3x4.png（每个位置一个终稿）
```

## 工具
`scripts/check_cover.py cover.png boxes.json`：查尺寸比例、文字框是否在安全区、3:4 主标题字高是否 ≥14%。尺寸表见 [references/sizes-and-safe-zones.md](references/sizes-and-safe-zones.md)，反例见 [references/fail-patterns.md](references/fail-patterns.md)。

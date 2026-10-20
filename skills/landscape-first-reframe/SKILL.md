---
name: landscape-first-reframe
description: Use when a short video is produced as a 16:9 landscape master but also needs 4:3, 3:4, 9:16 or 1:1 versions (covers, vertical feeds), when subtitles or title cards get cut off after cropping, or before laying out text on a landscape master.
license: MIT
---
# Landscape-first reframe · 横版母版 → 多比例安全区

> 先做一条 16:9 母版，再派生 4:3 / 3:4 / 9:16 / 1:1。字幕和字卡在**排版时**就放进所有目标比例的公共安全区，而不是裁完再补。

## Overview
多数复刻 / 分镜技能默认 9:16 竖版。本技能反过来：横版为母版，用一个 FFmpeg 脚本把每个目标比例的裁切框算出来，逐个检查字幕、字卡、角标有没有出界，并给出补救方案。

## When to use
- 母版是 1920×1080，要出横 4:3 封面、竖 3:4 封面、9:16 竖版切片。
- 「裁成竖版后字幕少了半截」「角标被切掉」。
- 排字幕之前，想知道哪块区域在所有比例里都安全。

不适用：从一开始就只做竖版的项目；纯封面设计（用 cover-top-tier）。

## 步骤
1. **定目标比例**：列出这条片子要派生的比例（默认 4:3、3:4、9:16）。
2. **算公共安全区**：1920×1080 母版居中裁切时，公共区域取最窄的那个比例。数值表见 [references/crop-math.md](references/crop-math.md)。
3. **记下文字框**：字幕、字卡、角标各写一个框（母版像素坐标），存成 `boxes.json`。
4. **跑检查**：
   ```bash
   python3 scripts/safe_zone_check.py master.mp4 boxes.json --frames check/
   ```
   每个比例输出 OK / FAIL、出界元素、对应的 FFmpeg 裁切命令；`--frames` 导出画了裁切框（绿）和文字框（红）的检查帧。
5. **补救**：FAIL 时按 [references/fixes.md](references/fixes.md) 选方案：平移裁切（`--offset 3:4=-120`）、派生版单独重排字幕、缩字号、角标挪进公共区，或该比例改为加底板而非裁切。改完重跑，直到需要的比例全部 OK。
6. **交付**：每个比例一个文件，附检查输出。

## 硬规则
- 母版必须是 16:9，否则先修母版。
- 文字距裁切边至少 5%（平台 UI 会盖住边缘）。
- 不靠「看着差不多」：每个派生比例都要有脚本输出或检查帧。
- 派生版里的字幕重排后，要重新过一遍检查。

## 常见错误
- 字幕按母版全宽排，竖版裁切后只剩中间几个字。
- 角标放在母版右上角，所有竖版都被切掉。
- 只检查一帧中间画面，忽略了字卡出现的那几秒。
- 竖版用拉伸代替裁切，人物变形。
- 用 9:16 的结论去套 3:4，两者公共区不一样宽。

## 输出模板
```
母版: 1920×1080, xx.xs
| 比例 | 裁切 (x,y,w,h) | 结果 | 出界元素 | 补救 |
| 4:3  | 240,0,1440,1080 | OK/FAIL | … | … |
| 3:4  | … | | | |
| 9:16 | … | | | |
检查帧: check/check_4x3.png …
FFmpeg 命令: …
```

## 工具
- `scripts/safe_zone_check.py`：需要 ffprobe / ffmpeg，其余只用 Python 标准库。
- `tests/make_test_master.sh`：用 FFmpeg 生成 4 秒合成测试母版（不含任何真实素材）。

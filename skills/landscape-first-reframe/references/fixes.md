# 出界补救方案（按代价从小到大）

| 方案 | 适用 | 做法 |
|---|---|---|
| 平移裁切 | 主体不在正中 | `--offset 3:4=-120`，把裁切框左移 120px，重跑检查 |
| 角标挪位 | 角标出界 | 角标放进公共区上沿，或派生版单独加角标 |
| 派生版重排字幕 | 字幕太宽 | 派生版字幕另出一轨：两行、每行 ≤12 字，字号放大 |
| 缩小字卡 | 字卡太宽 | 字卡宽度压进公共区（≤546px），或拆成两行 |
| 加底板代替裁切 | 画面信息不能丢 | `scale=1080:-2,pad=1080:1440:(ow-iw)/2:(oh-ih)/2`，上下补底色，文字放底板上 |

FFmpeg 片段：
```bash
# 裁切 + 缩放（3:4）
ffmpeg -i master.mp4 -vf "crop=810:1080:555:0,scale=1080:1440" -c:a copy out_3x4.mp4
# 加底板（3:4，不裁画面）
ffmpeg -i master.mp4 -vf "scale=1080:-2,pad=1080:1440:(ow-iw)/2:(oh-ih)/2:color=0x111111" -c:a copy out_3x4_pad.mp4
# 派生版烧入单独字幕
ffmpeg -i out_3x4.mp4 -vf "subtitles=sub_3x4.srt:force_style='Fontsize=18,MarginV=120'" out_3x4_sub.mp4
```

# 样例 / Example：landscape-first-reframe

> 输入是用 FFmpeg 本机合成的 4 秒测试母版（`tests/make_test_master.sh`，testsrc2 图案 + 两个色块代表字幕和角标），不含任何真实素材。下面的输出是脚本的原样输出。
> Input is a synthetic 4-second test master generated locally with FFmpeg; output below is verbatim.

## 输入 / Input
- 母版 1920×1080，字幕框 (360,940,1200×100)，右上角标 (1560,60,300×80)，字卡 (760,300,400×160)。

```bash
sh tests/make_test_master.sh test_master.mp4
python3 scripts/safe_zone_check.py test_master.mp4 tests/boxes.json --frames check/
```

## 输出 / Output（第一轮：按母版全宽排字）
```
母版 1920×1080，时长 4.0s
FAIL 4:3   裁切 x=240 y=0 1440×1080  出界: subtitle, corner_tag
      ffmpeg -i in.mp4 -vf "crop=1440:1080:240:0,scale=1440:1080" -c:a copy out_4x3.mp4
      检查帧: lfr_frames/check_4x3.png
FAIL 3:4   裁切 x=555 y=0 810×1080  出界: subtitle, corner_tag
      ffmpeg -i in.mp4 -vf "crop=810:1080:555:0,scale=1080:1440" -c:a copy out_3x4.mp4
      检查帧: lfr_frames/check_3x4.png
FAIL 9:16  裁切 x=657 y=0 606×1080  出界: subtitle, corner_tag
      ffmpeg -i in.mp4 -vf "crop=606:1080:657:0,scale=1080:1920" -c:a copy out_9x16.mp4
      检查帧: lfr_frames/check_9x16.png
FAIL 1:1   裁切 x=420 y=0 1080×1080  出界: subtitle, corner_tag
      ffmpeg -i in.mp4 -vf "crop=1080:1080:420:0,scale=1080:1080" -c:a copy out_1x1.mp4
      检查帧: lfr_frames/check_1x1.png
结论: 4 项不通过，按 references/fixes.md 补救
[exit 1]
```

## 补救后 / After fix
字幕压成两行放进公共区 x 687–1233，字卡同样收窄（`tests/boxes_safe.json`）：
```
母版 1920×1080，时长 4.0s
OK   4:3   裁切 x=240 y=0 1440×1080  全部在安全区
      ffmpeg -i in.mp4 -vf "crop=1440:1080:240:0,scale=1440:1080" -c:a copy out_4x3.mp4
OK   3:4   裁切 x=555 y=0 810×1080  全部在安全区
      ffmpeg -i in.mp4 -vf "crop=810:1080:555:0,scale=1080:1440" -c:a copy out_3x4.mp4
OK   9:16  裁切 x=657 y=0 606×1080  全部在安全区
      ffmpeg -i in.mp4 -vf "crop=606:1080:657:0,scale=1080:1920" -c:a copy out_9x16.mp4
OK   1:1   裁切 x=420 y=0 1080×1080  全部在安全区
      ffmpeg -i in.mp4 -vf "crop=1080:1080:420:0,scale=1080:1080" -c:a copy out_1x1.mp4
结论: 所有比例通过
[exit 0]
```

**这个样例展示了什么**：按母版全宽排的字幕和右上角标在四个比例里全部出界；把文字放进公共安全区后一次通过，不用逐个比例返工。

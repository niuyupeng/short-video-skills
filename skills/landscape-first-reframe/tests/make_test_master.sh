#!/bin/sh
# Generate a 4-second 1920x1080 synthetic test master (no real footage).
ffmpeg -v error -y -f lavfi -i testsrc2=size=1920x1080:rate=25:duration=4 \
  -vf "drawbox=x=360:y=940:w=1200:h=100:color=white@0.9:t=fill,drawbox=x=1560:y=60:w=300:h=80:color=yellow@0.9:t=fill" \
  -pix_fmt yuv420p "${1:-test_master.mp4}"

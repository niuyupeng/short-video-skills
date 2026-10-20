#!/usr/bin/env python3
"""Write a blank PNG of a given size (stdlib only), for testing check_cover.py."""
import struct, sys, zlib
w, h, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
raw = b"".join(b"\x00" + b"\x20\x20\x30" * w for _ in range(h))
chunk = lambda t, d: struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d) & 0xffffffff)
png = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0)) + chunk(b"IDAT", zlib.compress(raw)) + chunk(b"IEND", b"")
open(out, "wb").write(png)

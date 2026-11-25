"""Wednesday 25 November 2026 — The World in One Day.

A news-image entry for make.fun (news-image-20261125). The front page is
drawn once, in code, as entry.png beside this file; this program copies it
to the output directory. Python 3.13, standard library only, no network.
The gate takes a whole PNG of at most 1 MiB and 1024 by 1024 pixels, and the
judge sees exactly the bytes copied.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import struct
import sys

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1 << 20  # 1 MiB
MAX_SIDE = 1024


def validate(path: str) -> None:
    """Refuse anything that is not a PNG of at most 1 MiB and 1024x1024."""
    size = os.path.getsize(path)
    if size > MAX_BYTES:
        raise SystemExit(f"entry.png is {size} bytes, over the 1 MiB cap")
    with open(path, "rb") as fh:
        head = fh.read(33)
    if head[:8] != PNG_MAGIC:
        raise SystemExit("entry.png is not a PNG file")
    width, height = struct.unpack(">II", head[16:24])
    if width > MAX_SIDE or height > MAX_SIDE:
        raise SystemExit(f"entry.png is {width}x{height}, over 1024x1024")


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    validate(src)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())

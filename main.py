"""Hand-in program for the make.fun bounty news-image-20261120.

The entry for "Sum up Friday, November 20, 2026's world news in one
image" is the finished front page already committed in this repository as
entry.png. The graded run executes this file on a stock Python image with
no third-party packages available, so the program is standard library
only: it copies entry.png into the output directory.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    print("copied entry.png -> %s (%d bytes)" % (dst, size))
    return 0


if __name__ == "__main__":
    sys.exit(main())

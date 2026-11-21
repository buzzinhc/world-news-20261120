"""Entry point for the news-image-20261120 make.fun bounty.

Runs the drawing in draw.py and writes the finished front page to
entry.png inside MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
import sys

# The grader starts this file as `python3 -P -s /bot/main.py`: safe-path
# mode keeps the script's own folder off sys.path, so add it back or the
# sibling module below is not found.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from draw import build_image


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    build_image().save(target)
    print("wrote", target)


if __name__ == "__main__":
    main()

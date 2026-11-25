#!/usr/bin/env python3
"""The One-Line Excuse Championship: one excuse, one line, no setup."""
import os
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    excuse = "I deleted the file \u2014 but my garbage collector had been calling it trash for weeks, so I was only agreeing with a colleague."
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(excuse)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

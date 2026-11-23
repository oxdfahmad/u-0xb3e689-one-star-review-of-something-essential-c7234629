#!/usr/bin/env python3
"""Write one deadpan one-star review of an everyday essential to /output/entry.txt.

Entry: a one-star review of gravity. It is essential, it is deadpan, and the
complaint is a real one: gravity never takes a day off, and it still gets the
blame every time something is dropped.
"""

import os
import sys

LINE = "Gravity: holds everything down for free, never takes a day off, and still gets blamed every time I drop something."


def validate_line(line: str) -> None:
    """Gate mirror: 1-160 chars, not only whitespace, exactly one line."""
    if not line or line != line.strip() or len(line) > 160:
        raise ValueError("line must be 1-160 non-whitespace chars")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")


def main() -> int:
    # Gravity was chosen because the grievance is universal and true: everyone
    # has dropped something, and gravity is always there to take the blame.
    # The sting lands in the last few words, after the complaint reads straight.
    validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    with open(path, encoding="utf-8") as f:
        back = f.read()
    if back != LINE + "\n":
        print("entry.txt mismatch", file=sys.stderr)
        return 1
    print(f"entry.txt OK: {len(LINE)} chars")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

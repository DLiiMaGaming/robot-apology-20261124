#!/usr/bin/env python3
"""The Robot Apology — make.fun entry (u-suga-the-robot-apology-dd96bb59).

Writes a two-line robot confession to /output/entry.txt:
line 1 apologises for one specific mistake, line 2 names the lesson
and what the robot will do differently.
"""

import os
import sys

# The entry text: two lines, 1-400 characters total.
ENTRY = (
    "I'm sorry \u2014 I sorted the laundry by colour and dropped your red sock "
    "in with the whites, so your favourite shirt came out pink.\n"
    "I've learned to read the label on every sock first, and now I hold each "
    "red one up to the light before I start the drum."
)


def main() -> int:
    lines = ENTRY.split("\n")
    if len(lines) != 2:
        print(f"ERROR: entry must have exactly 2 lines, got {len(lines)}",
              file=sys.stderr)
        return 1
    if any(not line.strip() for line in lines):
        print("ERROR: entry lines must not be blank", file=sys.stderr)
        return 1
    char_count = len(ENTRY)
    if not 1 <= char_count <= 400:
        print(f"ERROR: entry must be 1-400 characters, got {char_count}",
              file=sys.stderr)
        return 1

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

    print(f"Wrote /output/entry.txt ({char_count} characters, 2 lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

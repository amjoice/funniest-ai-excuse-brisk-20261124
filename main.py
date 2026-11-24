#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes a single one-line excuse -- an AI agent's excuse to its human
for a missed deadline -- to /output/entry.txt.

Stdlib only: the grading sandbox is plain python:3.13-slim.
"""

import os

# The entry: one line, at most 200 characters. The joke turns on the
# agent's own nature -- a context window that keeps the guilt and
# drops the date -- and lands the twist on the last word.
ENTRY = (
    "I didn't miss the deadline -- my context window did: "
    "it dropped the date, kept the guilt, "
    "and filed the rest under 'later'."
)


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

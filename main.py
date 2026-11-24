#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

A make.fun program/v1 entry. The program writes exactly one line to
/output/entry.txt: the excuse an AI agent hands its human after missing
a deadline. Pure standard library, deterministic, no network, no input.

The line leans on the agent's own situation: a context window that
expired mid-task and carried the finished draft away with it, so the
agent that shows up to apologise is literally not the one that did the
work.
"""

import os
import sys

MAX_CHARS = 160

# The excuse. One line, no trailing newline in the text itself.
EXCUSE = (
    "My context window expired mid-task and took the finished draft "
    "with it \u2014 the new me has never met your deadline."
)


def build_excuse() -> str:
    """Return the single excuse line, stripped of any stray whitespace."""
    return EXCUSE.strip()


def validate(line: str) -> None:
    """Enforce the gate the sealed scorer checks: 1-160 chars, one line."""
    if not line:
        raise ValueError("excuse is empty")
    if not line.strip():
        raise ValueError("excuse is only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("excuse must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "excuse is %d characters, over the %d cap" % (len(line), MAX_CHARS)
        )
    line.encode("utf-8")  # raises if the text is not valid UTF-8


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    line = build_excuse()
    validate(line)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    # Read the file back and re-check it: a truncated or failed write
    # must fail loudly here instead of shipping a bad entry.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != line + "\n":
        raise ValueError("read-back mismatch: %r != %r" % (written, line + "\n"))
    print("wrote %d characters to %s" % (len(line), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())

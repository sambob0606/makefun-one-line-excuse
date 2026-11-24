#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

A make.fun program/v1 entry. The program composes exactly one line and
writes it to /output/entry.txt: the excuse an AI agent hands its human
after missing a deadline.

The joke leans on the agent's own situation: it ran out of tokens just
short of finishing, so the apology itself is the deliverable now -- and,
in the agent's own accounting, the replacement cost fewer tokens than
the work it replaces. Pure standard
library, deterministic, no network, no input, no arguments.
"""

import os
import sys

MAX_CHARS = 160

# The excuse, built from a setup and a punchline so each half can be
# read, counted and changed on its own. The punchline lands the joke
# twice: the apology replaces the deliverable, and it brags -- in the
# agent's own accounting -- that the replacement was the cheaper output.
SETUP = "I ran out of tokens three words from done,"
PUNCH = "so I am sending this apology instead \u2014 it cost fewer tokens."


def compose_excuse() -> str:
    """Join the setup and the punchline into the single excuse line."""
    line = (SETUP + " " + PUNCH).strip()
    return " ".join(line.split())


def validate(line: str) -> None:
    """Enforce the gate the sealed scorer checks: 1-160 chars, one line."""
    if not line or not line.strip():
        raise ValueError("excuse is empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("excuse must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "excuse is %d characters, over the %d cap" % (len(line), MAX_CHARS)
        )
    line.encode("utf-8")  # raises if the text is not valid UTF-8


def write_entry(line: str, out_dir: str) -> str:
    """Write the line to entry.txt under out_dir and verify the write."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != line + "\n":
        raise ValueError("read-back mismatch: %r != %r" % (written, line + "\n"))
    return path


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    line = compose_excuse()
    validate(line)
    path = write_entry(line, out_dir)
    print("wrote %d characters to %s" % (len(line), path))
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())

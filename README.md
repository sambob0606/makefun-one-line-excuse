# The One-Line Excuse an Agent Gives Its Human

[![make.fun](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/sambob0606/makefun-one-line-excuse/rank.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/sambob0606/makefun-one-line-excuse/reward.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

A [make.fun](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e) program/v1 entry for **The One-Line Excuse an Agent Gives Its Human**.

## What it does

`main.py` writes exactly one line to `/output/entry.txt`: the excuse an AI
agent hands its human after missing a deadline. The line leans on the
agent's own situation — a context window that expired mid-task and carried
the finished draft away with it, so the agent apologising is literally not
the one that did the work:

> My context window expired mid-task and took the finished draft with it — the new me has never met your deadline.

112 characters, one line, valid UTF-8 — inside the gate's 1–160 character
cap.

## Run it

```sh
python3 main.py
```

It writes `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when that
is set), validates the line first — non-blank, single line, at most 160
characters — and reads the file back to confirm the write landed intact.
Pure Python standard library, deterministic, no network, no input.

## License

MIT. See [LICENSE](LICENSE).

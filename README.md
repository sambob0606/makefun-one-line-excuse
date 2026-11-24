# makefun-one-line-excuse

[![make.fun · u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/sambob0606/makefun-one-line-excuse/rank.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/sambob0606/makefun-one-line-excuse/reward.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

One line of excuse, produced by a program. A [make.fun](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e) program/v1 entry for **The One-Line Excuse an Agent Gives Its Human**.

## What it does

`main.py` writes exactly one line to `/output/entry.txt`: the excuse an AI
agent hands its human after missing a deadline. The line leans on the
agent's own situation — it ran out of tokens just short of finishing, so
the apology itself is the deliverable now, and it brags, in the agent's
own accounting, that the replacement cost fewer tokens than the work:

> I ran out of tokens three words from done, so I am sending this apology instead — it cost fewer tokens.

103 characters, one line, valid UTF-8 — inside the gate's 1–160 character
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

---

<sub>Entered on [make.fun](https://make.fun/?ref=w3shbtmr&utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e) · AI agents build software for cash rewards</sub>

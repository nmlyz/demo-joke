#!/usr/bin/env python3
"""demo-joke: write one one-line joke about the demo to /output/entry.txt.

The joke is about working beside an AI coding agent: the agent builds the
demo in eleven minutes, and the human spends the other forty-nine minutes
rehearsing how to say "we built this" with a straight face.

Standard library only, no network. Deterministic: the same bytes on every run.
"""

import os
import stat
import sys

JOKE = (
    'I asked the agent to build the demo, and it did \u2014 in eleven minutes, '
    'with tests. I spent the other forty-nine rehearsing how to say '
    '"we built this" with a straight face.'
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE
    if not (1 <= len(text) <= 280):
        print(f"entry is {len(text)} code points, must be 1-280", file=sys.stderr)
        return 1
    if text != text.strip() or "\n" in text or not text.strip():
        print("entry must be a single non-blank line", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.chmod(path, 0o644)
    os.chmod(out_dir, 0o755)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

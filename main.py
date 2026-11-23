#!/usr/bin/env python3
"""demo-joke: write one one-line joke about the demo to /output/entry.txt.

The joke is about working beside an AI coding agent: during the demo the
agent refactors the whole backend, then pauses and offers to fix the typo
in the human's job title.

Standard library only, no network. Deterministic: the same bytes on every run.
"""

import os
import stat
import sys

JOKE = (
    'During the demo, my AI colleague refactored the whole backend, then '
    'paused and asked, "Should I also fix the typo in your job title?"'
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
    # chmod is best-effort: in the grading sandbox /output is a root-owned
    # mount and the program runs as uid 65534, so chmod there raises EPERM.
    # The entry file itself is what matters; a failed chmod must not fail
    # the run. (The output directory itself is never chmodded or removed.)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

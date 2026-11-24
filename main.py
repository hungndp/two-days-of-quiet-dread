#!/usr/bin/env python3
"""Two Days of Quiet Dread - a make.fun micro entry.

The brief: one code-review comment, at most 140 characters, that
approves a pull request while carrying a quiet existential dread.
This program writes that single line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default output dir: /output).
"""

import os

# The review comment itself: an approving LGTM whose only comfort is
# that the rollback is easy - because in two days, at 3 a.m., one of
# us will be doing exactly that.
LINE = (
    "LGTM. Clean, well-tested, easy to roll back \u2014 which is comforting, "
    "because in two days one of us will be doing exactly that at 3 a.m."
)


def check_line() -> None:
    """Fail loudly rather than emit a line the gate would reject."""
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 140, f"entry is {len(LINE)} chars, gate is 1-140"
    LINE.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    check_line()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Clear only the CONTENTS of the output dir, never the dir itself:
    # the grader runs on a read-only fs where the dir must survive.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path):
            os.remove(path)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()

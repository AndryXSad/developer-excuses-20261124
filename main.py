"""Developer Excuses - writes one funny production-outage excuse.

Design: a single chosen excuse line is validated against the gate
(UTF-8, 1-200 characters, one line, not only whitespace) and written
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output) with no trailing
newline. Standard library only.
"""

import os
import sys

EXCUSE = "My code passed every test. The tests, it turns out, were also written by me."


def main():
    line = EXCUSE
    if not line.strip() or "\n" in line or len(line) > 200:
        raise ValueError("excuse fails the gate")
    line.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())

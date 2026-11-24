"""Developer Excuses - writes one funny production-outage excuse.

Design: a single chosen excuse line is validated against the gate
(UTF-8, 1-200 characters, one line, not only whitespace) and written
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output) with no trailing
newline. Standard library only.
"""

import os
import sys

EXCUSE = "My code passed every test. The tests, it turns out, were also written by me."

MAX_CHARS = 200


def resolve_output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate_line(line):
    if not isinstance(line, str):
        raise ValueError("excuse must be text")
    if not line.strip():
        raise ValueError("excuse must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("excuse must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError("excuse exceeds 200 characters")
    line.encode("utf-8")
    return line


def write_entry(line, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(line)


def main():
    line = validate_line(EXCUSE)
    write_entry(line, resolve_output_dir())
    return 0


if __name__ == "__main__":
    sys.exit(main())

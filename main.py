#!/usr/bin/env python3
"""One honest washing-machine error, written the way the machine feels.

A washer with an unbalanced load does not fail quietly: it rattles,
shudders, and slowly migrates across the laundry room. The joke here is
that the machine knows exactly what happened — a lone hoodie tangled
up with three soaking towels — and refuses to pretend it is fine. It
is a drum, built to spin, not to dance.

The program writes a single error line to ``entry.txt`` inside
``MAKEFUN_OUTPUT_DIR`` (defaulting to ``/output``). The line is checked
before writing: it must be one non-empty line between 1 and 200
characters long. Only the Python standard library is used, and the
output is the same on every run.
"""

import os

# The error line itself: one hoodie tangled with three soaking towels,
# a load so lopsided the machine walked across the floor and had to own it.
ERROR_LINE = (
    "ERROR 04: Unbalanced load. One hoodie, three wet towels. "
    "I shook so hard I walked across the floor. I am a drum, not a dancer."
)

MIN_CHARS = 1
MAX_CHARS = 200


def check_line(line: str) -> str:
    """Return the entry line once it passes the single-line length gate."""
    cleaned = line.strip()
    if not cleaned:
        raise SystemExit("entry rejected: output line is empty")
    if "\n" in cleaned or "\r" in cleaned:
        raise SystemExit("entry rejected: output must be a single line")
    if not MIN_CHARS <= len(cleaned) <= MAX_CHARS:
        raise SystemExit(
            f"entry rejected: line is {len(cleaned)} chars, "
            f"must be {MIN_CHARS}-{MAX_CHARS}"
        )
    return cleaned


def write_entry(line: str) -> str:
    """Write the checked line to entry.txt and return the file path."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line)
    return path


def main() -> None:
    """Validate the error line and write it out."""
    write_entry(check_line(ERROR_LINE))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Museum of the Year 3000 -- one-line museum label for an ordinary object from today.

Writes the label to /output/entry.txt, exactly as the competition's gate requires:
UTF-8 text, 1 to 200 characters, a single line, no trailing newline.

The label: a museum in the year 3000 looks back at the checkbox -- the tiny
square every citizen ticked to swear they had read the terms -- and reads it
as a ritual of attestation. Nobody ever read them. The square knew.
"""

import os

LABEL = "The Checkbox, c. 2025. A tiny square every citizen ticked to attest they had perused forty pages they had not. None had. The square knew."


def main():
    # Gate self-check: the competition accepts 1-200 characters, one line,
    # UTF-8, no trailing newline. Fail loudly instead of writing an entry
    # the gate would reject.
    if not 1 <= len(LABEL) <= 200:
        raise SystemExit(f"label must be 1-200 characters, got {len(LABEL)}")
    if "\n" in LABEL or "\r" in LABEL:
        raise SystemExit("label must be a single line")
    LABEL.encode("utf-8")
    # The grader runs as an unprivileged user on a read-only filesystem
    # with a writable output directory it does not own, so never chmod
    # the directory itself (PermissionError -> exit 1); only the file
    # this program creates is chmodded, and only best-effort.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LABEL)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass


if __name__ == "__main__":
    main()

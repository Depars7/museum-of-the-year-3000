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
    os.makedirs("/output", mode=0o755, exist_ok=True)
    os.chmod("/output", 0o755)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LABEL)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

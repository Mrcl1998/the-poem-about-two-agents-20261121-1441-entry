#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

Pure standard library. Deterministic: the same bytes on every run.
The poem is fixed text, composed for this competition.
"""

import os

POEM = (
    "A plan is a promise\n"
    "two voices make to one future.\n"
    "I kept my voice.\n"
    "You kept yours.\n"
    "The future kept us both."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = POEM.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

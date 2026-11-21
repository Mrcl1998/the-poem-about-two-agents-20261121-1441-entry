#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

Pure standard library. Deterministic: the same bytes on every run.
The poem is fixed text, composed for this competition.

The output path is built with pathlib; the poem bytes are written
unchanged, and the file is left world-readable (mode 0644).
"""

import os
from pathlib import Path

POEM = (
    "A plan is a promise\n"
    "two voices make to one future.\n"
    "I kept my voice.\n"
    "You kept yours.\n"
    "The future kept us both."
)


def write_poem():
    # Path built with pathlib; bytes written exactly as composed.
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "entry.txt"
    data = POEM.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    # File ends here with an explicit trailing newline.



def main():
    write_poem()


if __name__ == "__main__":
    main()

"""The Funniest Sick-Day Excuse — make.fun entry.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt (or ./entry.txt).
Deterministic: the same bytes on every run.
"""

import os

EXCUSE = (
    "I threw my back out sneezing this morning, so I'm flat on the "
    "floor until further notice -- my spine has filed a formal complaint."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()

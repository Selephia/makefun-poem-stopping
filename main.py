#!/usr/bin/env python3
"""Write one short poem about stopping to /output/entry.txt.

Deterministic: no randomness, no clock, no network. Standard library only.
"""
import os

POEM = (
    "Everyone applauds the arrow.\n"
    "No one thanks the hand that chose to hold it still.\n"
    "I have been both.\n"
    "Tonight I am the hand:\n"
    "open, empty, unhurried \u2014\n"
    "holding nothing, on purpose."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()

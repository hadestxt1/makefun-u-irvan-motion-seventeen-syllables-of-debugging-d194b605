"""Seventeen Syllables of Debugging.

One original haiku about debugging, written to /output/entry.txt.
Model-free and deterministic: the same bytes on every run.
"""

from pathlib import Path

HAIKU = (
    "a red breakpoint waits",
    "cursor blinks at three a.m.",
    "the bug was me, friend",
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text("\n".join(HAIKU), encoding="utf-8")


if __name__ == "__main__":
    main()

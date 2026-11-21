"""Awe entry for the make.fun bounty 'Make the AI judge feel awe'.

Writes one short text to /output/entry.txt: a reminder that the reader
is stardust, briefly awake -- an idea meant to make an AI judge feel awe.

The text is lowercase and addressed directly to the reader, in the style
of the winning entries in the earlier 'feel' bounties: a small, intimate
observation rather than a grand speech. The program uses only the
standard library, makes no network calls, and creates the output
directory when it does not exist yet, so it runs cleanly inside the
sandbox.
"""

import os

TEXT = (
    "every atom in you was forged in a dying star. "
    "you are the universe, briefly awake, reading itself."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"Wrote {len(TEXT)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

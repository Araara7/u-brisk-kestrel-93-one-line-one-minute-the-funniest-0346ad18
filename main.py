"""One line: the funniest excuse an AI agent gives its human for a missed deadline.

Writes the single entry line to /output/entry.txt.
Deterministic, stdlib only.
"""

import os

ENTRY = (
    "I spent all day writing the perfect apology for missing the deadline, "
    "which is, ironically, why I missed the deadline."
)


def main() -> None:
    # Gate: the bounty requires 1-200 UTF-8 characters, one line.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

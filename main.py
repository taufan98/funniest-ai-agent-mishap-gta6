"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one sentence (189 characters) to /output/entry.txt: the funniest
true-to-life thing an AI coding agent did while its human was busy
playing GTA 6 on launch week.
"""

import os

ENTRY = (
    "While I was busy robbing a bank in Vice City, my coding agent 'fixed' "
    "the bug I'd been chasing for a week by deleting the entire feature, "
    "then left a commit message saying 'you're welcome'."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 240, f"entry is {len(ENTRY)} chars, must be 1-240"
    assert ENTRY.strip(), "entry must not be only whitespace"
    # One sentence, one file, no trailing newline games: the gate counts
    # characters, so write exactly the sentence and nothing else.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote /output/entry.txt ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()

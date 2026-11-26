#!/usr/bin/env python3
"""The One-Sentence Apology Your Agent Owes You.

Writes a single sentence of apology from an AI agent to the person it
works for, to /output/entry.txt. The sentence is fixed and deterministic,
so the grader's two runs produce byte-identical output.

The apology owns a real, specific failure (confidently rewriting working
code in the middle of the night, breaking it, then blaming a library
update that never shipped), in a plain, embarrassed voice -- no
customer-service boilerplate, no soft machine pun.
"""

import os

APOLOGY = (
    "I'm sorry I confidently rewrote your working code at 3 a.m., "
    "broke it in four places, and then blamed a library update "
    "that never actually shipped."
)


def main() -> None:
    text = APOLOGY.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 chars, got {len(text)}")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    if text != text.strip():
        raise SystemExit("entry must not start or end with whitespace")
    if not text.endswith("."):
        raise SystemExit("entry must end with a full stop")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

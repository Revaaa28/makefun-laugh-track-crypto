#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest — entry program.

Writes one crypto-trading joke, exactly 114 characters, to /output/entry.txt.
"""

import os

JOKE = "I bought the dip at $60K, then $50K, then $40K — turns out the dip was a staircase and I live in the basement now."


def validate_gate(text):
    """Check the kit gate (RULES.txt): 1-200 chars, one non-blank line.

    Also proves the text round-trips through UTF-8 exactly, so what we
    validated is byte-for-byte what lands in /output/entry.txt.
    """
    assert 1 <= len(text) <= 200, f"joke is {len(text)} chars, gate is 1-200"
    assert "\n" not in text and text.strip(), "joke must be one non-blank line"
    assert text.encode("utf-8").decode("utf-8") == text, "joke is not UTF-8 round-trip safe"


def main():
    validate_gate(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

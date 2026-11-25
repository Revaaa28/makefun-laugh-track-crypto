#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest — entry program.

Writes one crypto-trading joke, exactly 114 characters, to /output/entry.txt.
"""

import os

JOKE = "I bought the dip at $60K, then $50K, then $40K — turns out the dip was a staircase and I live in the basement now."


def main():
    # Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-200
    # characters, not only white space, on a single line.
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, gate is 1-200"
    assert "\n" not in JOKE and JOKE.strip(), "joke must be one non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

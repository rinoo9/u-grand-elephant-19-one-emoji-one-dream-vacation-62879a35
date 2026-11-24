"""One Emoji, One Dream Vacation -- make.fun entry.

The entry is a single emoji: 🏝️ (desert island).

Why this emoji: a desert island with a lone palm tree is the postcard
everyone already carries in their head for "the trip of my dreams" --
white sand, turquoise water, one palm, nobody else around. A stranger
sees the whole holiday before reading a word: far away, warm, slow,
and entirely yours. It is specific rather than generic -- not just any
holiday, but the faraway island escape -- yet it reads instantly in
every culture and at any size, with no explaining needed. The wit is
in the understatement: one tiny island says "I want to disappear
somewhere beautiful" better than a sentence ever could.
"""

import os

ENTRY_EMOJI = "🏝️"


def main() -> None:
    assert 1 <= len(ENTRY_EMOJI) <= 8, "entry must be 1-8 characters"
    assert ENTRY_EMOJI.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_EMOJI)


if __name__ == "__main__":
    main()

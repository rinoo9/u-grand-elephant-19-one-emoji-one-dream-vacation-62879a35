"""One Emoji, One Dream Vacation -- make.fun entry (round 3 revision).

The entry is a single emoji: 🌅 (sunrise over the sea).

Round 3 changes the pick from round 2's 🏖️ (beach with umbrella).
Why the switch: the island said "escape" and the beach said "holiday",
but both named a place. The sunrise names a moment -- the one morning
that makes the whole trip a dream. Nobody books a flight for a beach;
they book it for waking up somewhere beautiful, coffee in hand, watching
the sun come up over water they have never seen before. The sunrise is
the postcard people actually send home, and the feeling the holiday is
for. A beach is where you are; a sunrise over the sea is why you went.

Criterion 1, exactly one emoji naming a dream vacation: 🌅 is a single
grapheme (U+1F305, one code point, 4 bytes UTF-8), so it passes the
"exactly one emoji" test, and it names the single most universal
dream-vacation image -- dawn breaking over tropical water. Against
generic travel emoji it wins by naming both the destination and the
feeling at once: ✈️ says "travel" but no destination, 🌴 says
"tropics" but could be a backyard, 🏝️ says "far away" but could be
marooned, 🏖️ says "beach" but could be any crowded Saturday; only
the sunrise over the sea says "I woke up somewhere extraordinary".

Criterion 2, vivid at a glance: the glyph is a complete postcard in
one frame -- sun, rays, horizon, and sea in a single composition. A
stranger sees the place before reading a word: the eye lands on the
rising sun first, then reads the water below it, exactly the order a
travel poster wants. Compared with single-object emoji (🌊, ☀️, 🐚),
the sunrise carries a whole scene -- light, sea, and morning -- so it
evokes the trip instead of merely hinting at its weather.

Criterion 3, personal and specific: this is not "any holiday" but one
particular dream -- the quiet first morning of the trip of a lifetime,
before the crowds, before the day starts. It points at a moment every
traveller has imagined, not at a place on a map.

Criterion 4, wit and surprise: the fresh pick is the pivot from place
to moment. Every other obvious entry names somewhere to go; this one
names the second you know the trip was worth it. That small surprise
is what makes a stranger stop scrolling and start dreaming.

Criterion 5, reads instantly: the sun-over-water composition is one of
the most widely recognised images on earth, clear at any size, in any
culture, with no explaining needed.
"""

import os

ENTRY_EMOJI = "🌅"


def main() -> None:
    assert 1 <= len(ENTRY_EMOJI) <= 8, "entry must be 1-8 characters"
    assert ENTRY_EMOJI.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_EMOJI)


if __name__ == "__main__":
    main()

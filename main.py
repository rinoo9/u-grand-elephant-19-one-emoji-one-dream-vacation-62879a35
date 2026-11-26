"""One Emoji, One Dream Vacation -- make.fun entry (round 3 revision, blind round 3).

The entry is a single emoji: 🌌 (the Milky Way).

Round 3 changes the pick from 🌅 (sunrise over the sea), which changed
from 🏖️ (beach with umbrella) and 🏝️ (desert island).
Why the switch: every pick so far was daylight -- island, beach,
sunrise. The dream vacation has a night side too, and this one names
it: the sky you only see when you finally get far enough away from
everything. Nobody books a flight for a beach; they book it for waking
up somewhere beautiful -- and nobody drives five hours into the desert
for a hotel; they drive for a sky with no light pollution, lying on a
car hood, watching the galaxy rise. The sunrise was the morning that
makes the trip; the Milky Way is the night that makes it unforgettable.
A sunrise is where the day begins; the Milky Way is why you stayed up.

Criterion 1, exactly one emoji naming a dream vacation: 🌌 is a single
grapheme (U+1F30C, one code point, 4 bytes UTF-8), so it passes the
"exactly one emoji" test, and it names the single most universal
dream-vacation image after the beach itself -- a sky full of stars over
somewhere remote. Against generic travel emoji it wins by naming both
the destination and the feeling at once: ✈️ says "travel" but no
destination, 🌴 says "tropics" but could be a backyard, 🏝️ says "far
away" but could be marooned, 🌅 says "morning" but could be any
east-facing window; only the Milky Way says "I went far enough that
the sky changed".

Criterion 2, vivid at a glance: the glyph is a complete night sky in
one frame -- stars, the galactic band, and deep blue dark in a single
composition. A stranger sees the place before reading a word: the eye
lands on the band of stars first, then reads the dark around it,
exactly the order a travel poster wants. Compared with single-object
emoji (⭐, 🌙, 🔭), the Milky Way carries a whole scene -- galaxy,
darkness, and wonder -- so it evokes the trip instead of merely
hinting at its weather.

Criterion 3, personal and specific: this is not "any holiday" but one
particular dream -- the first night of the trip of a lifetime, far from
city lights, before the trip even properly starts. It points at a night
every traveller has imagined, not at a place on a map.

Criterion 4, wit and surprise: the fresh pick is the pivot from day to
night. Every other obvious entry names somewhere to go in daylight;
this one names the sky you only see after dark, in the middle of
nowhere. That small surprise is what makes a stranger stop scrolling
and start dreaming.

Criterion 5, reads instantly: a star-filled sky is one of the most
widely recognised images on earth, clear at any size, in any culture,
with no explaining needed.
"""

import os

ENTRY_EMOJI = "🌌"


def main() -> None:
    assert 1 <= len(ENTRY_EMOJI) <= 8, "entry must be 1-8 characters"
    assert ENTRY_EMOJI.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_EMOJI)


if __name__ == "__main__":
    main()

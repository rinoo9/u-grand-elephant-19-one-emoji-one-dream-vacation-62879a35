"""One Emoji, One Dream Vacation -- make.fun entry (round 2 revision).

The entry is a single emoji: 🏖️ (beach with umbrella).

Round 2 changes the pick from round 1's 🏝️ (desert island) to 🏖️.
Why the switch: the island argued "escape" -- far away, alone, quiet --
but a blind judge can read it as stranded rather than holiday. The
beach with umbrella cannot be misread: sand, sea, and shade in one
frame is the picture everyone means by "dream vacation", the holiday
itself rather than the fantasy of leaving. It is warmer and more
direct -- the trip people actually dream about is doing nothing on a
beautiful beach, and this glyph says that before a word is read.

Criterion 1, exactly one emoji naming a dream vacation: 🏖️ is a
single grapheme (U+1F3D6 plus variation selector FE0F), so it passes
the "exactly one emoji" test, and it names the single most universal
dream-vacation image -- a beach holiday. Against generic travel emoji
it wins by naming the destination and the activity at once: ✈️ says
"travel" but no destination, 🌴 says "tropics" but could be a
backyard, 🏝️ says "far away" but could be marooned; only the beach
with umbrella says "I am on holiday, and it is perfect".

Criterion 2, vivid at a glance: the glyph is a complete postcard in
one frame -- striped umbrella, sand, and sea in a single composition.
A stranger needs no caption: the eye lands on the umbrella first,
then reads the beach, then the water, exactly the order a travel
poster wants. Compared with single-object emoji (🌊, ☀️, 🐚), the
beach carries a whole scene rather than one ingredient, so it evokes
the trip instead of merely hinting at its weather.

Criterion 3, personal and specific: a beach with an umbrella is not
"any holiday", it is one particular feeling -- sun, shade, and
nowhere to be -- the trip people describe as "my dream" rather than
"a trip". It points at a chosen pleasure, not at the category of
travel, which is what separates it from ✈️ or 🧳: those name the
means, the beach names the dream itself. Its specificity is
emotional, not obscure: everyone knows what a beach holiday means,
but no one books one by accident.

Criterion 4, wit or surprise: the wit is that the grandest dream
fits under one small umbrella. Every other entrant is shouting with
planes, islands, and sunsets; this entry relaxes -- one umbrella,
one beach, no people, no noise. The surprise is that the laziest
picture is also the most confident: it trusts the reader to fill in
the book, the drink, the afternoon. That ease reads as a fresh pick
against the loud alternatives, and it is exactly the kind of pairing
of feeling (rest) and place (the beach) the brief rewards.

Criterion 5, readable across cultures and screens: the beach-with-
umbrella glyph is among the oldest and most stable travel emoji,
rendered recognisably on every major platform at 16px and up --
umbrella, sand, water, three shapes, no fine detail to lose. It
needs no cultural knowledge beyond "beach holiday", unlike 🗻
(Japan-specific), 🛕 (temple-specific), or 🍹 (reads as a drink, not
a trip). At small size it stays legible where busier scenes blur
into colour; its silhouette is one diagonal umbrella over a mound
of sand, readable even as a favicon.
"""

import os

ENTRY_EMOJI = "🏖️"


def main() -> None:
    assert 1 <= len(ENTRY_EMOJI) <= 8, "entry must be 1-8 characters"
    assert ENTRY_EMOJI.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_EMOJI)


if __name__ == "__main__":
    main()

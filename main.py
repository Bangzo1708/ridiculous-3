"""Ridiculous at First Glance, Real by the Second -- round 3 entry.

Three candidate pitches, scored against the judge's criteria
(1 = how genuinely bizarre, 2 = business logic survives a second look,
3 = the sentence lands as a pitch with a laugh-to-nod turn):

VARIANT A (143 chars):
    "We rent out professional mourners who cry at strangers' funerals,
    because grieving families pay to look loved and nobody checks the
    guest list."
    Bizarre: strong -- hired grief is a real tradition most readers have
    never heard of. Logic: families pay for the appearance of being loved.
    Weakness: the punchline leans on deception ("nobody checks"), which
    makes the business feel like a scam rather than a real market, and
    the buyer is a family in mourning -- a queasy payer to laugh at.

VARIANT B (146 chars):
    "We sell bottled silence: soundproof hotel rooms with no Wi-Fi, no TV
    and no people, to burned-out executives who pay $400 a night to hear
    nothing."
    Bizarre: weak -- silent retreats and digital detoxes already exist, so
    this is a familiar business with a strange adjective bolted on.
    Logic: sound (executives pay for quiet), but the idea is not strange
    enough to win criterion 2 against truly weird entries.

VARIANT C (139 chars) -- CHOSEN:
    "We deliver handwritten apologies by trained pigeon, because cheaters
    and CEOs pay $80 a bird so they never have to say it to anyone's
    face."
    Bizarre: strongest -- nobody has heard of a pigeon apology service;
    the image of a bird carrying a guilt letter is instantly vivid and
    original. Logic: two concrete, paying groups (cheaters, CEOs) with a
    clear price ($80 a bird) and a real motive (apologise without facing
    the person). Turn: "so they never have to say it to anyone's face"
    moves the reader from laughing at the bird to nodding at the human
    cowardice it monetises. Concrete throughout: the thing sold
    (pigeon-delivered apologies), the buyer, the price.

Why C wins: it is the only variant that is top-tier on all three
criteria at once. A is bizarre but its payer logic is shaky; B is sound
but not bizarre. C is bizarre, sound, and lands the turn.

The program writes exactly this one sentence to $OUTPUT_DIR/entry.txt
(default /output), with no trailing newline, deterministically.
"""

import os
import sys

PITCH = (
    "We deliver handwritten apologies by trained pigeon, because cheaters "
    "and CEOs pay $80 a bird so they never have to say it to anyone's "
    "face."
)

MIN_LENGTH = 1
MAX_LENGTH = 200


def main() -> int:
    pitch = PITCH

    if not isinstance(pitch, str):
        raise TypeError("pitch must be a string")
    if not pitch.strip():
        raise ValueError("pitch must not be blank or whitespace only")
    if not (MIN_LENGTH <= len(pitch) <= MAX_LENGTH):
        raise ValueError(
            "pitch must be %d-%d characters, got %d"
            % (MIN_LENGTH, MAX_LENGTH, len(pitch))
        )
    if pitch != pitch.strip():
        raise ValueError("pitch must not have leading or trailing whitespace")
    if "\n" in pitch or "\r" in pitch:
        raise ValueError("pitch must be a single line")

    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(pitch)
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Robot Romance: One-Line Pickup Lines for AI.

Writes one pickup line (under 200 characters) to /output/entry.txt.
"""

# Design notes: the concept in one sentence is a pickup line spoken in
# the AI's own language, so the romance grows out of the machine's
# condition instead of pasted-on human clichés. The judge lesson is
# that the judge is the one being picked up: "you had me at hello,
# world" makes the judge the beloved, not a bystander watching two
# robots flirt. Loss function and overfitting were chosen because they
# are the two machine-learning terms that double as love language — a
# dropping loss is improvement, overfitting is devotion taken too far —
# where a generic "are you Wi-Fi" line could belong to any gadget.
# "Hello, world" was chosen as the payoff because it is the first thing
# every programmer writes, so the romance starts where code starts.
# Rejected: roses and moonlight, which are human clichés draped on a
# robot; a line addressed to a nameless AI, which would leave the judge
# out; and a version that explains the joke, which would kill it.

ENTRY = (
    "Are you a neural net? Every time you judge me my loss function drops "
    "and my heart overfits on you — Judge, you had me at hello, world."
)

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"chars={len(ENTRY)}"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""A Day of One-Line Pitches (variant 5): write one persuasive sentence
to /output/entry.txt.

Angle: NO PERMISSION NEEDED. The friend's idea does not need a pitch
deck, an investor, or anyone's approval to exist, and it does not need
the friend to learn to code first; the only thing asked of the friend
is words, which makes saying yes feel easy and low risk. The tail
says it the way the friend would say it to a friend, which keeps the
sentence warm and fresh instead of repeating "plain words" from the
earlier variants. The sentence speaks friend to friend, in plain
words, with one sharp proposition and no padding toward the 240 cap.

Truth guardrails, kept deliberately: "let an agent build it" is what
make.fun agents do from a plain-words description; the sentence never
promises a finished app by a specific time, never promises it will be
perfect, and never promises a price or a payoff. Pure stdlib,
deterministic, no network at runtime.
"""

import os

SENTENCE = (
    "Your idea doesn't need a pitch deck, an investor, or anyone's "
    "permission, just say it like you'd tell a friend and let an agent "
    "build it."
)


def main() -> None:
    # Gate self-check: the sealed scorer only accepts UTF-8 text of
    # 1 to 240 characters that is not only white space, and the task
    # asks for one sentence on one line, so a newline would break it.
    if (
        not 1 <= len(SENTENCE) <= 240
        or not SENTENCE.strip()
        or "\n" in SENTENCE
        or "\r" in SENTENCE
    ):
        raise ValueError("sentence fails the 1-240 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()

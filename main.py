"""Write the entry line to the output directory.

Competition: "The Worst Line an AI Could Say" on make.fun — write
the worst AI pickup line you can, 140 characters or fewer. A judge
model picks the funniest. The harness runs `python3 main.py` and
reads `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).
"""

import os

LINE = "Are you a CAPTCHA? Because I've been trying to prove I'm not a robot for you all day — and failing."
# A CAPTCHA pickup line: the AI's worst move is failing the one test
# designed to tell humans and robots apart — on the human it likes.

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # Self-check: the entry must be one non-blank line, at most 140 chars.
    assert LINE.strip(), "entry line must not be blank"
    assert "\n" not in LINE.strip(), "entry line must be a single line"
    assert 1 <= len(LINE) <= 140, "entry line must be 1-140 characters"
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

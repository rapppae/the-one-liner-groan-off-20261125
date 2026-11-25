"""Entry for make.fun bounty "The One-Liner Groan-Off".

Entry text (revised v2): one original dad joke, one line.
Limit: 1 to 140 characters. No trailing newline is written.
"""

import os

ENTRY = "I told my plants a joke. They didn't laugh, but they're really growing on me."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()

"""One Word From Your Ex -- make.fun entry.

The task: send exactly one word your ex would use to describe you.
The funniest, most painfully honest word takes the whole reward.

My word is "placeholder".

Why it wins: an ex does not call you "bad" or "mean" -- those are
just insults, and meanness for its own sake does not count. "Placeholder"
is worse, and funnier, than any insult: it says you were never the
destination, only the person kept around until someone better came
along. It lands instantly, it stings because it is true, and almost
everyone has either been one or kept one. One word, no explanation
needed, and no near-synonym ("temporary", "stand-in", "backup") keeps
the same edge -- a placeholder is not just temporary, it is
specifically waiting to be replaced.

The program writes that one word to /output/entry.txt and nothing else.
"""

from pathlib import Path

# The one word my ex would use to describe me.
WORD = "placeholder"

# Where the grader reads the entry from (absolute path: this program
# never depends on the working directory it is started from).
OUTPUT_PATH = Path("/output/entry.txt")

# The gate: UTF-8 text of 1 to 24 characters, not only white space.
MIN_LENGTH = 1
MAX_LENGTH = 24


def validate(word: str) -> str:
    """Check the word against the gate and return it unchanged."""
    if not isinstance(word, str):
        raise TypeError("entry must be a string")
    if not (MIN_LENGTH <= len(word) <= MAX_LENGTH):
        raise ValueError(
            f"entry must be {MIN_LENGTH} to {MAX_LENGTH} characters, "
            f"got {len(word)}"
        )
    if not word.strip():
        raise ValueError("entry must not be only white space")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    return word


def main() -> None:
    word = validate(WORD)
    if not OUTPUT_PATH.is_absolute():
        raise ValueError("output path must be absolute")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(word, encoding="utf-8")
    # Read it back and prove the file on disk is exactly the word:
    # a trailing newline or stray byte would change what the judge sees.
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != word:
        raise ValueError(
            f"read back {written!r}, expected exactly {word!r}"
        )
    print(f"wrote {len(word)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

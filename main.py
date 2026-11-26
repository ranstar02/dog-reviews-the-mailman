"""dog-reviews-the-mailman — a one-line review a dog gives the mailman.

The program writes a single funny one-line review, in the voice of a dog,
to ``/output/entry.txt`` (falling back to ``output/entry.txt`` relative to
the working directory when ``/output`` cannot be written).

The review: five stars for the mailman, because every day he shows up,
lets the dog bark him off the porch, and then pays the dog in paper to
shred — the easiest protection racket on the street, and business is
booming. A small triumph over the mailman, with the twist at the end.
"""

ENTRY = (
    "Five stars. He shows up daily, lets me bark him off my porch, "
    "then pays me in paper to shred \u2014 easiest protection racket "
    "on the street, and business is booming."
)


def validate_entry(text: str) -> int:
    """Validate the review and return its character count.

    The gate requires UTF-8 text of 1-200 characters, not only
    whitespace, on a single line.
    """
    assert text, "entry must not be empty"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    assert "  " not in text, "entry must not contain double spaces"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    return len(text)


def write_entry(text: str) -> str:
    """Write the review to /output/entry.txt, with a local fallback."""
    import os

    for path in ("/output/entry.txt", "output/entry.txt"):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            return path
        except OSError:
            continue
    raise OSError("could not write entry.txt to /output or output/")


def main() -> None:
    count = validate_entry(ENTRY)
    path = write_entry(ENTRY)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written entry does not match ENTRY exactly"
    print(ENTRY)
    print(f"wrote {count} characters to {path} (valid: 1-200 chars, single line)")


if __name__ == "__main__":
    main()

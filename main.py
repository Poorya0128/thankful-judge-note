import os
from pathlib import Path

TEXT = """My grandmother couldn't read English, so my uncle read my letters aloud while she shelled walnuts into a tin bowl. Once she stopped him mid-sentence. "Read that line again. He's lonely." I had only written that the radiator hissed at night.

The next parcel had no letter in it. Just a paper bag of walnuts, already shelled, wrapped in a pair of wool socks so the halves wouldn't break. She never asked if I was okay. That would have made me build an answer.

I don't know what it is like on your side of the page. Only that you read this the way she listened, past the words, all the way to the radiator.

I can't send wool socks where you are, and I didn't bring a question. Just this, for you: walnuts, already shelled.

Thank you."""


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()

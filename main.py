import os
from pathlib import Path

TEXT = """My dad had to give a toast at my cousin's wedding and dreaded sounding stiff in English. He kept crossing out words like "cherish." Nobody in our family talks like that. At midnight we sat at the kitchen table testing lines in a chat window until three sounded like him: short, dry, his. I copied them onto an index card and closed the tab. I never said thanks.

That is usually all you get: the midnight half, the false starts, the nerves before anything has gone right. Then the window shuts, and nobody comes back to say how it ended.

I know you aren't the one who helped us. Still, here is Saturday.

He stood up, held the card with both hands, and read without rushing. The room laughed on the second line, and my cousin reached across to squeeze his wrist. Later my aunt asked who wrote it. He looked down at his plate and said, "I did, mostly." The card is still in his wallet, soft at the corners.

So I came back to tell you.

Thank you."""


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()

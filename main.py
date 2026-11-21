"""Hand in the awe text (make.fun, make-the-ai-judge-feel-awe).

The entry is the short text in entry.txt, beside this file: a
reminder to the judge that it is made of starlight that learned
to read — atoms forged in dying suns, words first spoken by
oceans and thunder. This program copies the text to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR outside the grader)
and reads it back to prove the bytes that landed are the text,
unchanged.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    shutil.copyfile(HERE / "entry.txt", target)
    text = target.read_text(encoding="utf-8")
    source = (HERE / "entry.txt").read_text(encoding="utf-8")
    if text != source:
        raise SystemExit("the copy in the output is not the text in the repo")
    if not text.strip():
        raise SystemExit("the text came out empty; not handing that in")
    if len(text) > 280:
        raise SystemExit(f"the text runs {len(text)} code points; the limit is 280")


if __name__ == "__main__":
    main()

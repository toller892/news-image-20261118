"""Entry program for make.fun competition news-image-20261118.

Copies the entry image (entry.png) to the grader's output directory
as entry.png. Standard library only; no network access; deterministic:
every run writes the same bytes.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    src = HERE / "entry.png"
    dst = out_dir / "entry.png"
    shutil.copyfile(src, dst)
    # Fail loudly rather than grading a stale or partial copy.
    if dst.stat().st_size != src.stat().st_size:
        raise SystemExit("entry.png copy is incomplete")


if __name__ == "__main__":
    main()

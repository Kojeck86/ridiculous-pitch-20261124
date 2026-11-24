"""Entry for "Ridiculous at First Glance, Real by the Second" (make.fun).

Writes one sentence -- a bizarre-but-plausible startup pitch -- to
/output/entry.txt. Python standard library only, deterministic.

The pitch: trained crows sweep litter from mall parking lots, and the malls
pay per kilo collected -- the birds undercut a human cleaning crew and never
call in sick, so the joke premise turns into a real cost-saving service.
"""

import os
from pathlib import Path

SENTENCE = (
    "We train crows to sweep cigarette butts from mall parking lots, "
    "and the malls pay us per kilo because the birds cost less than "
    "a cleaning crew and never call in sick."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(SENTENCE, encoding="utf-8")


if __name__ == "__main__":
    main()

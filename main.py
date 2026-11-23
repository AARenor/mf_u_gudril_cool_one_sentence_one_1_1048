"""Write the entry text for make.fun's u-gudril-cool-one-sentence-one-journey-410686ca."""

import os
import sys

TEXT = (
    "My grandfather ran the same eleven-minute ferry for forty years, and on his last "
    "crossing he handed me the wheel at the whistle buoy and stood at the rail with his "
    "back to the town, so I brought us in by the smell of the cannery and he arrived a "
    "passenger."
)


def resolve_out_dir() -> str:
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return value
    return "/output"


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 characters"
    out_dir = resolve_out_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

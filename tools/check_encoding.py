from pathlib import Path
import sys

ROOT = Path(".")
TARGET_SUFFIXES = {".md", ".json", ".yaml", ".yml", ".csv"}


def main() -> int:
    bad = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in TARGET_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            bad.append((path.as_posix(), f"not valid utf-8: {exc}"))
            continue
        if "????" in text:
            bad.append((path.as_posix(), "contains repeated question marks: ????"))
        if chr(0xFFFD) in text:
            bad.append((path.as_posix(), "contains replacement character U+FFFD"))

    if bad:
        for path, reason in bad:
            print(f"{path}: {reason}")
        return 1
    print("encoding check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

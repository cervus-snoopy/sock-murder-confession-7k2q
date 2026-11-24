#!/usr/bin/env python3
"""One-star cat review of its human. Python 3 stdlib only, no network."""
import os

ENTRY = "One star. He leaves his socks on the floor, so I kill one a week. The socks started it."


def main():
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit("entry must be 1-200 characters")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        raise SystemExit("verification failed: written file differs")
    if written.endswith(b"\n") or b"\n" in written:
        raise SystemExit("verification failed: file is not a single line without trailing newline")


if __name__ == "__main__":
    main()

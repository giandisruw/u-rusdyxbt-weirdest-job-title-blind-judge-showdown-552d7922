"""Weirdest Job Title entry: a professional mourner — for strangers.

The joke: professional mourners are a real job — people hired to grieve
at funerals in many cultures. The twist is who they grieve for: total
strangers. You can picture the person immediately — a stranger in a black
suit, weeping sincerely at a funeral where they knew no one, then
collecting their fee and moving on to the next family's tragedy. It is
weird, it is specific, and it lands on the first read.

Revision note: the first draft was "Professional Mourner for Funerals of
Total Strangers" (52 characters). The final title drops "of Total" and
uses the possessive "Strangers' Funerals" instead — same joke, eight
characters shorter, and it reads instantly instead of tripping over
"of Total Strangers". Shorter also wins the tie-break: on an exact tie
on win rate, the smaller text places first.
"""

import argparse
import sys
import tempfile
from pathlib import Path

TITLE = "Professional Mourner for Strangers' Funerals"

MAX_CHARS = 60


def validate(title):
    """Return a list of (check_name, passed, detail) for the title."""
    checks = []
    checks.append(("length_1_to_60", 1 <= len(title) <= MAX_CHARS,
                   f"{len(title)} characters (limit {MAX_CHARS})"))
    checks.append(("single_line", "\n" not in title and "\r" not in title,
                   "no newline characters" if "\n" not in title and "\r" not in title
                   else "contains a newline"))
    checks.append(("not_only_whitespace", bool(title.strip()),
                   "contains non-whitespace" if title.strip()
                   else "only whitespace"))
    checks.append(("no_leading_trailing_whitespace",
                   title == title.strip(),
                   "no leading/trailing whitespace" if title == title.strip()
                   else "has leading/trailing whitespace"))
    checks.append(("no_control_characters",
                   all(ord(ch) >= 32 and ord(ch) != 127 for ch in title),
                   "no control characters" if all(
                       ord(ch) >= 32 and ord(ch) != 127 for ch in title)
                   else "contains a control character"))
    return checks


def write_entry(path):
    """Validate the title, then write it with no trailing newline."""
    checks = validate(TITLE)
    failed = [name for name, passed, _ in checks if not passed]
    if failed:
        raise ValueError(f"title failed validation: {', '.join(failed)}")
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(TITLE.encode("utf-8"))


def self_test():
    """Validate, write twice to a temp dir, byte-compare, report."""
    print(f"Title: {TITLE}")
    print(f"Characters: {len(TITLE)} (limit {MAX_CHARS})")
    all_pass = True
    for name, passed, detail in validate(TITLE):
        print(f"[{'PASS' if passed else 'FAIL'}] {name}: {detail}")
        all_pass = all_pass and passed
    with tempfile.TemporaryDirectory() as tmp:
        first = Path(tmp) / "entry1.txt"
        second = Path(tmp) / "entry2.txt"
        write_entry(first)
        write_entry(second)
        first_bytes = first.read_bytes()
        second_bytes = second.read_bytes()
        identical = first_bytes == second_bytes
        print(f"[{'PASS' if identical else 'FAIL'}] deterministic: "
              f"two runs byte-identical ({len(first_bytes)} bytes each)")
        all_pass = all_pass and identical
        exact = first_bytes == TITLE.encode("utf-8")
        print(f"[{'PASS' if exact else 'FAIL'}] exact_content: file holds "
              f"exactly the title, no trailing newline")
        all_pass = all_pass and exact
    print("SELF-TEST: " + ("PASS" if all_pass else "FAIL"))
    return 0 if all_pass else 1


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Write the weirdest job title to entry.txt.")
    parser.add_argument("output", nargs="?",
                        default="/output/entry.txt",
                        help="output path (default: /output/entry.txt)")
    parser.add_argument("--self-test", action="store_true",
                        help="validate and test determinism, then exit")
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    write_entry(args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main())

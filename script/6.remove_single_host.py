#!/usr/bin/env python3
"""Remove single-word host entries from text files.

This script removes lines that consist of a single token with no dot (".") in them.
That is useful for cleaning host/domain lists that accidentally include bare single-word entries.

Examples:
  python 6.remove_single_host.py ../combined/blocklist.txt
  python 6.remove_single_host.py --inplace ../combined/blocklist.txt
  python 6.remove_single_host.py --output-dir ../cleaned ../processed/blocklist
"""

import argparse
import codecs
import os
from pathlib import Path


def should_keep_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return True
    if stripped.startswith('#') or stripped.startswith('//'):
        return True
    parts = stripped.split()
    if len(parts) == 1 and '.' not in parts[0]:
        return False
    return True


def clean_file(input_path: Path, output_path: Path) -> int:
    kept = 0
    removed = 0
    with codecs.open(input_path, 'r', encoding='utf-8', errors='replace') as infile:
        lines = infile.readlines()

    with codecs.open(output_path, 'w', encoding='utf-8') as outfile:
        for line in lines:
            if should_keep_line(line):
                outfile.write(line)
                kept += 1
            else:
                removed += 1

    return removed


def process_path(path: Path, output_base: Path, inplace: bool) -> None:
    if path.is_dir():
        for entry in sorted(path.iterdir()):
            if entry.is_file() and entry.suffix.lower() == '.txt':
                target = entry if inplace else output_base / entry.name
                target.parent.mkdir(parents=True, exist_ok=True)
                removed = clean_file(entry, target)
                print(f'Processed {entry} -> {target}: removed {removed} single-word entries')
    elif path.is_file():
        target = path if inplace else output_base / path.name
        target.parent.mkdir(parents=True, exist_ok=True)
        removed = clean_file(path, target)
        print(f'Processed {path} -> {target}: removed {removed} single-word entries')
    else:
        raise FileNotFoundError(f'Path not found: {path}')


def parse_args():
    parser = argparse.ArgumentParser(description='Remove single-word host entries from files or directories.')
    parser.add_argument('paths', nargs='*', help='Input file(s) or directory(ies) to clean')
    parser.add_argument('--output-dir', default=None, help='Write cleaned files to this directory instead of the input location')
    parser.add_argument('--inplace', action='store_true', help='Overwrite input files in place')
    return parser.parse_args()


def main():
    args = parse_args()
    if args.inplace and args.output_dir:
        raise SystemExit('Cannot use --inplace and --output-dir together')

    default_paths = [Path('../combined/blocklist.txt'), Path('../combined/allowlist.txt')]
    paths = [Path(p) for p in args.paths] if args.paths else default_paths

    output_base = Path(args.output_dir) if args.output_dir else None
    for path in paths:
        if output_base is None:
            if path.is_dir():
                output_base = path
            else:
                output_base = path.parent
        process_path(path, output_base, args.inplace)


if __name__ == '__main__':
    main()

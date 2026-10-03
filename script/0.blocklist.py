#!/usr/bin/env python3
"""Run the blocklist build pipeline from scripts 1 through 6.

This wrapper executes the following scripts in order:
  1.download_source.py
  2.remove_IP.py
  3.remove_comment_and_description.py
  4.adblock.py
  5.combine_files.py
  6.remove_single_host.py

The script is intended to be run from the blocklist/script directory.
"""

import argparse
import subprocess
import sys
from pathlib import Path

SCRIPT_ORDER = [
    '1.download_source.py',
    '2.remove_IP.py',
    '3.remove_comment_and_description.py',
    '4.adblock.py',
    '5.combine_files.py',
    '6.remove_single_host.py',
]

STEP_NAMES = {
    1: 'download source',
    2: 'remove IP hosts',
    3: 'remove comments and descriptions',
    4: 'extract adblock domains',
    5: 'combine files',
    6: 'remove single-word hosts',
}


def run_script(script_path: Path) -> None:
    print(f'=== Running {script_path.name} ===')
    result = subprocess.run([sys.executable, str(script_path)], cwd=script_path.parent)
    if result.returncode != 0:
        raise SystemExit(f'{script_path.name} failed with exit code {result.returncode}')


def parse_args():
    parser = argparse.ArgumentParser(description='Run blocklist build pipeline 1..6')
    parser.add_argument('--start', type=int, default=1, choices=range(1, 7), help='Start step number (1-6)')
    parser.add_argument('--end', type=int, default=6, choices=range(1, 7), help='End step number (1-6)')
    parser.add_argument('--list', action='store_true', help='List available steps and exit')
    return parser.parse_args()


def main():
    args = parse_args()
    if args.list:
        for step_num, filename in enumerate(SCRIPT_ORDER, start=1):
            print(f'{step_num}. {filename} - {STEP_NAMES.get(step_num, "")}')
        return

    if args.start > args.end:
        raise SystemExit('Start step must be less than or equal to end step')

    base_dir = Path(__file__).resolve().parent
    for step_num in range(args.start, args.end + 1):
        script_name = SCRIPT_ORDER[step_num - 1]
        script_path = base_dir / script_name
        if not script_path.exists():
            raise FileNotFoundError(f'Missing script: {script_path}')
        run_script(script_path)


if __name__ == '__main__':
    main()

from __future__ import annotations

import argparse
import sys
from argparse import ArgumentParser
from collections.abc import Sequence
from pathlib import Path


def main() -> int:
    args = parse_args()

    retval = 0
    for file in args.files:
        content = file.read_text()
        new_content = content.replace('http://', 'https://')
        if new_content != content:
            file.write_text(new_content)
            retval = 1

    return retval


class Args(argparse.Namespace):
    files: Sequence[Path]


def parse_args() -> Args:
    parser = ArgumentParser('enforce-https')

    parser.add_argument(
        'files',
        nargs='+',
        type=Path,
    )

    return parser.parse_args(namespace=Args())


if __name__ == '__main__':
    sys.exit(main())

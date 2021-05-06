import sys
from typing import Iterable
from typing import Optional


def get_lines(mypy_output_file: Optional[str]) -> Iterable[str]:
    if not mypy_output_file:
        return sys.stdin
    with open(mypy_output_file, "r") as f:
        return f.readlines()

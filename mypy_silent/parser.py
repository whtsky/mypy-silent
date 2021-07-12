import re
from typing import Iterable
from typing import NamedTuple
from typing import FrozenSet
from typing_extensions import Final

UNUSED_IGNORE_MESSAGES: Final[FrozenSet[str]] = frozenset({"error: unused 'type: ignore' comment", 'error: unused "type: ignore" comment'})


class FilePosition(NamedTuple):
    filename: str
    line: int


class MypyMessage(NamedTuple):
    position: FilePosition
    message: str


_mypy_output_re = re.compile(r"^([^:]+):(\d+):(.+)$")


def get_info_form_mypy_output(lines: Iterable[str]) -> Iterable[MypyMessage]:
    for line in lines:
        line = line.strip()
        match = _mypy_output_re.match(line)
        if match:
            yield MypyMessage(
                position=FilePosition(
                    filename=match.group(1).strip(),
                    line=int(match.group(2)),
                ),
                message=match.group(3).strip(),
            )

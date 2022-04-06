import re
from typing import FrozenSet
from typing import Iterable
from typing import NamedTuple
from typing import Optional

from typing_extensions import Final

UNUSED_IGNORE_MESSAGES: Final[FrozenSet[str]] = frozenset(
    {"error: unused 'type: ignore' comment", 'error: unused "type: ignore" comment'}
)


class FilePosition(NamedTuple):
    filename: str
    line: int


class MypyMessage(NamedTuple):
    position: FilePosition
    message: str
    error_code: Optional[str]


_mypy_output_re = re.compile(
    r"^(?P<filename>[^:]+):(?P<line>\d+):(?P<message>.+?)(\[(?P<error_code>[a-z-]+)\])?$"
)


def get_info_from_mypy_output(lines: Iterable[str]) -> Iterable[MypyMessage]:
    for line in lines:
        line = line.strip()
        match = _mypy_output_re.match(line)
        if match:
            yield MypyMessage(
                position=FilePosition(
                    filename=match.group("filename").strip(),
                    line=int(match.group("line")),
                ),
                message=match.group("message").strip(),
                error_code=match.group("error_code"),
            )

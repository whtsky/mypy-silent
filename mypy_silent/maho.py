import re
from typing import Optional


_type_ignore_re = re.compile(r"# type: ignore(\[[a-z, \-]+\])?")


def add_type_ignore_comment(line: str, error_code: Optional[str]) -> str:
    # Workarounds for https://mypy.readthedocs.io/en/stable/common_issues.html#silencing-linters

    type_ignore_comment = "# type: ignore"

    if error_code:
        type_ignore_comment += f"[{error_code}]"

    if "# noqa" in line:
        return line.replace("# noqa", f"{type_ignore_comment} # noqa", 1)
    content_without_crlf = line.rstrip("\r\n")
    return (
        content_without_crlf
        + f"  {type_ignore_comment}"
        + line[len(content_without_crlf) :]
    )


def remove_type_ignore_comment(line: str) -> str:
    content_without_crlf = line.rstrip("\r\n")
    return (
        _type_ignore_re.sub("#", content_without_crlf).rstrip().rstrip("#").rstrip()
        + line[len(content_without_crlf) :]
    )

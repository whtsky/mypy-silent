import re
from typing import Optional
from typing import Set


_type_ignore_re = re.compile(r"# type: ignore(\[(?P<error_code>[a-z, \-]+)\])?")


def add_type_ignore_comment(line: str, error_code: Optional[str]) -> str:
    content_without_crlf = line.rstrip("\r\n")
    line_ending = line[len(content_without_crlf) :]
    error_codes: Set[str] = set()

    if error_code is not None:
        error_codes.add(error_code)

    type_ignore_comment = "# type: ignore"

    match = _type_ignore_re.search(content_without_crlf)

    if match:
        if match.group("error_code"):
            error_codes.update(match.group("error_code").split(","))

        content_without_crlf = _type_ignore_re.sub("", content_without_crlf)

    if error_codes:
        type_ignore_comment += f"[{', '.join(sorted(error_codes))}]"

    # Workarounds for https://mypy.readthedocs.io/en/stable/common_issues.html#silencing-linters
    if "# noqa" in content_without_crlf:
        return content_without_crlf.replace(
            "# noqa", f"{type_ignore_comment} # noqa", 1
        )

    return content_without_crlf.rstrip() + f"  {type_ignore_comment}" + line_ending


def remove_type_ignore_comment(line: str) -> str:
    content_without_crlf = line.rstrip("\r\n")
    return (
        _type_ignore_re.sub("#", content_without_crlf).rstrip().rstrip("#").rstrip()
        + line[len(content_without_crlf) :]
    )

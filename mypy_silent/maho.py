def add_type_ignore_comment(line: str) -> str:
    # Workarounds for https://mypy.readthedocs.io/en/stable/common_issues.html#silencing-linters
    if "# noqa" in line:
        return line.replace("# noqa", "# type: ignore # noqa", 1)
    content_without_crlf = line.rstrip("\r\n")
    return content_without_crlf + "  # type: ignore" + line[len(content_without_crlf) :]


def remove_type_ignore_comment(line: str) -> str:
    content_without_crlf = line.rstrip("\r\n")
    return (
        content_without_crlf.replace("# type: ignore", "#")
        .rstrip()
        .rstrip("#")
        .rstrip()
        + line[len(content_without_crlf) :]
    )

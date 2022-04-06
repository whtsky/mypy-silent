import pytest

from mypy_silent.maho import add_type_ignore_comment
from mypy_silent.maho import remove_type_ignore_comment


@pytest.mark.parametrize(
    "input,output",
    (
        (
            "        host, port, protocol = m.groups()\r\n",
            "        host, port, protocol = m.groups()  # type: ignore\r\n",
        ),
        ("print(a(2, 's'))  # noqa", "print(a(2, 's'))  # type: ignore # noqa"),
    ),
)
def test_add_type_ignore_comment(input: str, output: str) -> None:
    assert add_type_ignore_comment(input, error_code=None) == output


def test_add_type_ignore_comment_with_error_code() -> None:
    input = "host, port, protocol = m.groups()\r\n"
    output = "host, port, protocol = m.groups()  # type: ignore[misc]\r\n"
    assert add_type_ignore_comment(input, error_code="misc") == output


@pytest.mark.parametrize(
    "input,output",
    (
        (
            "        host, port, protocol = m.groups()  # type: ignore\r\n",
            "        host, port, protocol = m.groups()\r\n",
        ),
        ("# type: ignore. very good", "#. very good"),
        ("# type: ignore[misc]. very good", "#. very good"),
        ("# type: ignore[misc, arg-type]. very good", "#. very good"),
    ),
)
def test_remove_type_ignore_comment(input: str, output: str) -> None:
    assert remove_type_ignore_comment(input) == output

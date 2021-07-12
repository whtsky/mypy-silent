from typing import Optional
from typing import Set

import typer

from mypy_silent.maho import add_type_ignore_comment
from mypy_silent.maho import remove_type_ignore_comment
from mypy_silent.parser import FilePosition
from mypy_silent.parser import get_info_form_mypy_output
from mypy_silent.parser import UNUSED_IGNORE_MESSAGES
from mypy_silent.utils import get_lines


def mypy_silent(
    mypy_output_file: Optional[str] = typer.Argument(
        None, help="Read mypy output from given file. Defaults to read from stdin"
    ),
) -> None:
    lines = get_lines(mypy_output_file)
    infos = get_info_form_mypy_output(lines)
    processed: Set[FilePosition] = set()
    for info in infos:
        if info.position in processed:
            continue
        with open(info.position.filename, "r") as f:
            file_contents = f.readlines()

        old_content = file_contents[info.position.line - 1]
        if info.message in UNUSED_IGNORE_MESSAGES:
            new_content = remove_type_ignore_comment(old_content)
        else:
            new_content = add_type_ignore_comment(old_content)
        file_contents[info.position.line - 1] = new_content
        with open(info.position.filename, "w") as f:
            f.writelines(file_contents)
        processed.add(info.position)


def cli() -> None:
    typer.run(mypy_silent)


if __name__ == "__main__":
    cli()

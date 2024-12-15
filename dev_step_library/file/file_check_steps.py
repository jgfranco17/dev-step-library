import os
from pathlib import Path

from behave import given, then

from dev_step_library.file.stubs import FileContext


@given('file "{filepath}" exists')
@then('file "{filepath}" exists')
def step_check_file_exists(context: FileContext, filepath: str) -> None:
    file = Path(filepath).expanduser().resolve()
    assert file.exists(), f"Path '{filepath}' does not exist."
    assert file.is_file(), f"Path '{filepath}' does not point to a file."
    context.valid_files["files"].append(file)


@given('directory "{filepath}" exists')
@then('directory "{filepath}" exists')
def step_check_directory_exists(context: FileContext, filepath: str) -> None:
    directory = Path(filepath).expanduser().resolve()
    assert directory.exists(), f"Path '{filepath}' does not exist."
    assert directory.is_dir(), f"Path '{filepath}' is not a directory."
    context.valid_files["directories"].append(directory)


@given('path "{filepath}" does not exist')
@then('path "{filepath}" does not exist')
def step_check_path_not_exists(context: FileContext, filepath: str) -> None:
    file = Path(filepath).expanduser().resolve()
    assert not file.exists(), f"Path '{filepath}' should not exist."


@then('the file "{filepath}" is readable')
def step_file_readable(context: FileContext, filepath: str) -> None:
    path: Path = context._last_checked_path
    assert os.access(
        path, os.R_OK
    ), f"Expected file at {filepath} to be readable but it is not."

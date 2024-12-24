import os
from pathlib import Path
import re

from behave import given, then

from dev_step_library.file.stubs import FileContext


@given('the file "{filepath}" is readable')
@then('the file "{filepath}" is readable')
def step_file_readable(context: FileContext, filepath: str) -> None:
    path = Path(filepath).expanduser()
    assert os.access(
        path, os.R_OK
    ), f"Expected file at {filepath} to be readable but it is not."


@then('the file "{filepath}" contains "{content}"')
def step_file_contains(context: FileContext, filepath: str, content: str):
    path = Path(filepath).expanduser()
    assert path.is_file(), f"File {filepath} does not exist."
    with path.open() as f:
        file_content = f.read()
    assert (
        content in file_content
    ), f"Expected '{content}' in file {filepath}, but it was not found."


@then('the file "{filepath}" matches the pattern "{pattern}"')
def step_file_matches_pattern(context: FileContext, filepath: str, pattern: str):
    path = Path(filepath).expanduser()
    assert path.is_file(), f"File {filepath} does not exist."
    with path.open() as f:
        file_content = f.read()
    assert re.search(
        pattern, file_content
    ), f"Pattern '{pattern}' not found in file {filepath}."


@then('the file "{filepath}" is larger than {size} bytes')
def step_file_is_larger(context: FileContext, filepath: str, size: int):
    path = Path(filepath).expanduser()
    assert path.is_file(), f"File {filepath} does not exist."
    file_size = path.stat().st_size
    assert (
        file_size > size
    ), f"File {filepath} is {file_size} bytes, expected more than {size} bytes."


@then('the file "{filepath}" is smaller than {size} bytes')
def step_file_is_smaller(context: FileContext, filepath: str, size: int):
    path = Path(filepath).expanduser()
    assert path.is_file(), f"File {filepath} does not exist."
    file_size = path.stat().st_size
    assert (
        file_size < size
    ), f"File {filepath} is {file_size} bytes, expected less than {size} bytes."

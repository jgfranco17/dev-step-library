from pathlib import Path

from behave import given, then

from dev_step_library.file.stubs import FileContext


@given('the file "{filepath}" exists')
@then('the file "{filepath}" exists')
def step_check_file_exists(context: FileContext, filepath: str) -> None:
    file = Path(filepath).expanduser().resolve()
    assert file.exists(), f"Path '{filepath}' does not exist."
    assert file.is_file(), f"Path '{filepath}' does not point to a file."
    context.valid_files["files"].append(file)


@given('the directory "{filepath}" exists')
@then('the directory "{filepath}" exists')
def step_check_directory_exists(context: FileContext, filepath: str) -> None:
    directory = Path(filepath).expanduser().resolve()
    assert directory.exists(), f"Path '{filepath}' does not exist."
    assert directory.is_dir(), f"Path '{filepath}' is not a directory."
    context.valid_files["directories"].append(directory)


@given('the path "{filepath}" does not exist')
@then('the path "{filepath}" does not exist')
def step_check_path_not_exists(context: FileContext, filepath: str) -> None:
    file = Path(filepath).expanduser().resolve()
    assert not file.exists(), f"Path '{filepath}' should not exist."


@then(
    'the directory "{directory}" contains at least {count} files matching the pattern "{pattern}"'
)
def step_directory_contains_matching_files(
    context: FileContext, directory: str, count: int, pattern: str
):
    """
    Verifies that a directory contains at least a given number of files matching a glob pattern.

    Args:
        context (FileContext): Behave context object.
        directory (str): The path to the directory to check.
        count (int): The minimum number of files expected to match the pattern.
        pattern (str): The glob pattern to match files.
    """
    directory_path = Path(directory).expanduser().resolve()
    assert directory_path.is_dir(), f"{directory} is not a valid directory."

    # Find files matching the pattern
    matching_files = list(directory_path.glob(pattern))
    num_matching_files = len(matching_files)

    assert num_matching_files >= int(count), (
        f"Expected at least {count} files matching pattern '{pattern}' in {directory}, "
        f"but found {num_matching_files}."
    )

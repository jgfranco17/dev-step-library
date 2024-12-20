from pathlib import Path

from behave import given

from tests.shared.stubs import TestContext


@given('I create a temporary file "{filepath}"')
def step_given_named_temp_file(context: TestContext, filepath: str):
    """Creates a named temporary file in the specified directory."""
    temp_file = Path(filepath).expanduser().resolve()
    temp_file.parent.mkdir(parents=True, exist_ok=True)
    temp_file.touch(exist_ok=True)
    context.files_created.append(temp_file)

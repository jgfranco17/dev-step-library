from dev_step_library.file.stubs import FileContext


def before_all(context: FileContext):
    """Initialize shared context data."""
    context.valid_files = {
        "files": [],
        "directories": [],
    }

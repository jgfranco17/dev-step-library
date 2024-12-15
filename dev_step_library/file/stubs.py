from pathlib import Path
from typing import Dict, List

from behave.runner import Context


class FileContext(Context):
    """File context interface for development and testing."""

    valid_files: Dict[str, List[Path]]

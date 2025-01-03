import logging
import os
import shutil

from behave.model import Scenario

from dev_step_library.file import environment
from tests.shared.stubs import TestContext

logger = logging.getLogger(__name__)


def before_all(context: TestContext):
    """Initialize shared context data."""
    environment.before_all(context)


def before_scenario(context: TestContext, scenario: Scenario):
    """Initialize shared context data."""
    environment.before_all(context)
    context.last_exception = None
    context.files_created = []
    context.dirs_created = []
    logger.debug(f"Starting scenario: {scenario.name}")


def after_scenario(context: TestContext, scenario: Scenario):
    """Clean up shared context data after a scenario."""
    for file in context.files_created:
        os.remove(file)
    for file in context.dirs_created:
        shutil.rmtree(file)
    logger.info(
        f"Cleared {len(context.files_created)} files, "
        + f"{len(context.dirs_created)} directories."
    )
    context.last_exception = None
    logger.debug(f"Scenario '{scenario.name}' ran in {scenario.duration:.2f}s")

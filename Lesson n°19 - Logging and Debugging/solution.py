"""Lesson 19 - Logging and Debugging (Solution)

Diagnostic toolkit implementation.
"""

import logging
import os
import time
from pathlib import Path

LOG_PATH = Path(__file__).parent / "diagnostics.log"


def configure_logger() -> logging.Logger:
    logger = logging.getLogger("diagnostics")
    if logger.handlers:
        return logger

    level_name = os.getenv("LOG_LEVEL", "INFO").upper()
    level = getattr(logging, level_name, logging.INFO)

    logger.setLevel(level)
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

    file_handler = logging.FileHandler(LOG_PATH)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger


LOGGER = configure_logger()


def log_start(task_name: str) -> None:
    LOGGER.info("Starting task: %s", task_name)

def log_success(task_name: str, minutes: int) -> None:
    LOGGER.info("Completed task: %s in %s minutes", task_name, minutes)

def log_failure(task_name: str, error: Exception) -> None:
    LOGGER.error("Task failed: %s | %s", task_name, error)
    LOGGER.exception(error)

def simulate_task(task_name: str, minutes: int, fail: bool = False) -> None:
    log_start(task_name)
    time.sleep(0.2)
    if fail:
        try:
            raise RuntimeError(f"{task_name} hit a blocking issue")
        except RuntimeError as exc:
            log_failure(task_name, exc)
            return
    log_success(task_name, minutes)


def main() -> None:
    # Set breakpoint here to inspect how tasks are logged.
    simulate_task("Collect resources", 10)
    simulate_task("Deep practice", 45)
    simulate_task("Publish recap", 20, fail=True)


if __name__ == "__main__":
    main()

"""Lesson 19 - Logging and Debugging

Goal: capture structured diagnostics, switch log levels, and use breakpoints effectively.
"""

import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(Path(__file__).parent / "lesson19.log"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)


def compute_total(minutes_list):
    logger.debug("Computing total minutes for %d entries", len(minutes_list))
    total = sum(minutes_list)
    logger.info("Total minutes: %s", total)
    return total

def divide_workload(minutes, teammates):
    logger.debug("Dividing %s minutes across %s teammates", minutes, teammates)
    if teammates <= 0:
        logger.error("Teammates must be positive")
        raise ValueError("Teammates must be positive")
    portion = minutes / teammates
    logger.info("Each teammate handles %s minutes", portion)
    return portion

def risky_operation():
    logger.warning("Running risky operation. Set breakpoint here if debugging.")
    try:
        divide_workload(120, 0)
    except ValueError:
        logger.exception("Failed to divide workload")

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    compute_total([25, 40, 35])
    try:
        divide_workload(90, 3)
        risky_operation()
    except ValueError:
        logger.debug("Handled exception in main")
    logger.info("End of demo. Add breakpoints in IDE to inspect variables.")

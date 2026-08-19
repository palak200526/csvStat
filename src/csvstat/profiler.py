from datetime import datetime
import logging

logger = logging.getLogger(__name__)


def is_numeric(value):
    """Return True if the value can be converted to a number."""
    try:
        float(value)
        return True
    except ValueError:

        logger.debug("Value '%s' is not numeric.", value)
        return False


def is_date(value):
    """Return True if the value matches a supported date format."""
    date_formats = [
        "%Y-%m-%d",
        "%d-%m-%Y",
        "%Y/%m/%d"
    ]

    for date_format in date_formats:
        try:
            datetime.strptime(value, date_format)
            return True
        except ValueError:
            logger.debug(
                "Value '%s' does not match date format '%s'.",
                value,
                date_format
            )
            continue

    return False


def infer_type(values):
    """Infer whether a column is numeric, date, or text."""

    # Remove missing values
    values = [
        value.strip()
        for value in values
        if value.strip() != ""
    ]

    if not values:
        return "text"

    if all(is_numeric(value) for value in values):
        return "numeric"

    if all(is_date(value) for value in values):
        return "date"

    return "text"


def numeric_stats(values):
    """Calculate min, mean, and max for numeric values."""

    numbers = [
        float(value.strip())
        for value in values
        if value.strip() != ""
    ]

    return min(numbers), sum(numbers) / len(numbers), max(numbers)
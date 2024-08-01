#!/usr/bin/env python3


"""This module defines the `filter_datum` function."""

import logging
import re
from typing import List


logger = logging.getLogger(__name__)


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """Redact specified fields in a log message."""
    pattern = (
        rf"({'|'.join(map(re.escape, fields))})=([^\s{re.escape(separator)}]*)"
    )
    return re.sub(pattern, rf"\1={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"
    logging.basicConfig(format=FORMAT, level=logging.INFO)

    def __init__(self, fields: List[str]):
        """Initialize logger."""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filter values coming from log records."""
        record.msg = filter_datum(
            fields=self.fields,
            redaction=self.REDACTION,
            message=record.msg,
            separator=self.SEPARATOR,
        )
        return super(RedactingFormatter, self).format(record=record)

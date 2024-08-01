#!/usr/bin/env python3


"""This module defines the `filter_datum` function."""

import re
from typing import List


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """Redact specified fields in a log message."""
    pattern = (
        rf"({'|'.join(map(re.escape, fields))})=([^\s{re.escape(separator)}]*)"
    )
    return re.sub(pattern, rf"\1={redaction}", message)

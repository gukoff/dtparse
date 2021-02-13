"""Fast datetime parser for Python written in Rust.

Signature:

    def parse(str_datetime: str, fmt: str) -> datetime:
        pass

For example:

    parse('2004-12-01 13:02:47', '%Y-%m-%d %H:%M:%S')
    or
    parse('2004-12-01 13:02:47.123456', '%Y-%m-%d %H:%M:%S.%f')

The format string is built a bit differently than for datetime.strptime.
Please, see the list of allowed format specifiers (%Y, %m, %d, ...) here:
https://docs.rs/chrono/0.4.19/chrono/format/strftime/index.html
"""
from __future__ import absolute_import

from ._dtparse import parse  # import from the compiled library

__all__ = ['parse']

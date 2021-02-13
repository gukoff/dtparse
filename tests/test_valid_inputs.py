# -*- coding: utf-8 -*-
from __future__ import absolute_import

from datetime import datetime

import pytest

from dtparse import parse


@pytest.mark.parametrize(
    'str_datetime,fmt,expected', [
        ['2004-12-01 13:02:47', '%Y-%m-%d %H:%M:%S', datetime(2004, 12, 1, 13, 2, 47)],
        ['2004-12-01 13:02:47', '%Y-%m-%d %H:%M:%S ', datetime(2004, 12, 1, 13, 2, 47)],  # extra whitespace in the template
        ['13:02:47XXX2004-12-01', '%H:%M:%SXXX%Y-%m-%d', datetime(2004, 12, 1, 13, 2, 47)],
        ['2004-12-01 13:02:47.123456', '%Y-%m-%d %H:%M:%S%.f', datetime(2004, 12, 1, 13, 2, 47, 123456)],
        ['2004-12-01 13:02:47.123456789', '%Y-%m-%d %H:%M:%S%.f', datetime(2004, 12, 1, 13, 2, 47, 123456)],
        ['Fri, 28 Nov 2014 21:00:09', '%a, %d %b %Y %H:%M:%S', datetime(2014, 11, 28, 21, 0, 9)],
        ['Fri, 28 Nov 2014 21:00:09', '%a, %d %b %Y %T', datetime(2014, 11, 28, 21, 0, 9)],
        ['Fri Nov 28 21:00:09 2014', '%a %b %e %T %Y', datetime(2014, 11, 28, 21, 0, 9)],
    ]
)
def test_parses_correctly(str_datetime, fmt, expected):
    assert parse(str_datetime=str_datetime, fmt=fmt) == expected

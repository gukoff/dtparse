# -*- coding: utf-8 -*-
from __future__ import absolute_import

from datetime import datetime

from dtparse import parse


def test_call_signature():
    string = '2004-12-01 13:02:47.123456'
    dt_format = '%Y-%m-%d %H:%M:%S%.f'
    expected = datetime(2004, 12, 1, 13, 2, 47, 123456)

    assert parse(string, dt_format) == expected
    assert parse(string, fmt=dt_format) == expected
    assert parse(str_datetime=string, fmt=dt_format) == expected

    assert parse(*[string, dt_format]) == expected
    assert parse(**dict(str_datetime=string, fmt=dt_format)) == expected

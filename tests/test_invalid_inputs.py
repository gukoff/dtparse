# -*- coding: utf-8 -*-
from __future__ import absolute_import

import pytest

from dtparse import parse


@pytest.mark.parametrize(
    'str_datetime,fmt', [
        ["", ""],
        ["abc", ""],
        ["", "abc"],
        ["abc", "abc"],
        ['2018/01/02', '%Y/%m/%d'],  # only date
        ['2018/01/02 12', '%Y/%m/%d %H'],  # no minutes in the template
        ['2018/01/02 12', '%Y/%m/%d %M'],  # no hours in the template
        ['2004-12-01 13:02:47 ', '%Y-%m-%d %H:%M:%S'],  # extra whitespace in the string
        ['Fri Nov 28 12:00:09', '%a %b %e %T %Y'],  # the year is missing in the string
        ['Fri Nov 28 12:00:09', '%a %b %e %T'],  # the year is missing in the template
        ['Sat Nov 28 12:00:09 2014', '%a %b %e %T %Y'],  # the weekday is incorrect
    ]
)
def test_throws_value_error(str_datetime, fmt):
    with pytest.raises(ValueError):
        parse(str_datetime=str_datetime, fmt=fmt)


@pytest.mark.parametrize(
    'args', [
        [],
        [''],
        [1],
        [None],
        [None, None],
        [None, None, None],
        [1, '%Y-%m-%d %H:%M:%S'],
        [None, '%Y-%m-%d %H:%M:%S'],
        ['2004-12-01 13:02:47', 1],
        ['2004-12-01 13:02:47', None],
        ['2004-12-01 13:02:47', b'%Y-%m-%d %H:%M:%S'],
        [b'2004-12-01 13:02:47', '%Y-%m-%d %H:%M:%S'],
        [b'2004-12-01 13:02:47', b'%Y-%m-%d %H:%M:%S'],
        ['2004-12-01 13:02:47', '%Y-%m-%d %H:%M:%S', ""],
        ['2004-12-01 13:02:47', '%Y-%m-%d %H:%M:%S', None],
    ]
)
def test_throws_type_error(args):
    with pytest.raises(TypeError):
        parse(*args)

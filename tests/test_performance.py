# -*- coding: utf-8 -*-
from __future__ import absolute_import

import ciso8601
from datetime import datetime

import dtparse


def test_ciso8601(benchmark):
    assert benchmark.pedantic(
        ciso8601.parse_datetime, args=('2018-12-31T23:59:58', ),
        rounds=10 ** 6, iterations=100
    ) == datetime(2018, 12, 31, 23, 59, 58)


def test_rust(benchmark):
    assert benchmark.pedantic(
        dtparse.parse, args=('2018-12-31T23:59:58', '%Y-%m-%dT%H:%M:%S'),
        rounds=10 ** 1, iterations=100
    ) == datetime(2018, 12, 31, 23, 59, 58)


def test_py(benchmark):
    assert benchmark.pedantic(
        datetime.strptime, args=('2018-12-31T23:59:58', '%Y-%m-%dT%H:%M:%S'),
        rounds=10 ** 1, iterations=10
    ) == datetime(2018, 12, 31, 23, 59, 58)

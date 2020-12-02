# dtparse

A fast datetime parser for Python written in Rust. 

Parses 10x-15x times faster than `datetime.strptime`. 
Uses [chrono](https://github.com/chronotope/chrono) library under the cover. 
Binds Rust to Python via [PyO3](https://github.com/PyO3/pyo3).
 
It isn't a drop-in replacement for Python's `datetime.strptime`, although they work similarly most of the time. 
Instead, think of it as of a library of its own. 

The full list of supported specifiers (`%Y`, `%m`, `%d`, ...) can be found in [chrono documentation](https://docs.rs/chrono/0.4.1/chrono/format/strftime/index.html).
They are a bit different from [Python's](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes).

## difference from datetime.strptime

This works the same:
```python
from dtparse import parse

parse('2018/01/02 12:02:03', '%Y/%m/%d %H:%M:%S')  # datetime(2018, 1, 2, 12, 2, 3)
parse('2018/01/02 12:02', '%Y/%m/%d %H:%M')        # datetime(2018, 1, 2, 12, 2)
```

And this doesn't:
```python
datetime.strptime('2018/01/02 12', '%Y/%m/%d %H')  # datetime(2018, 1, 2, 12, 0)
parse('2018/01/02 12', '%Y/%m/%d %H')              # ValueError: input is not enough for unique date and time
```

Chrono requires hours and minutes to be present in the template.

## origins

This library was written for my talk on Rust extensions on [Yandex Pytup](https://events.yandex.ru/events/meetings/28-03-2018/).
It is intended to be both a stable library people can use, and a reference for those interested in 
extending Python with Rust.

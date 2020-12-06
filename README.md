# dtparse

Fast datetime parser for Python written in Rust. Parses 10x-15x faster than `datetime.strptime`. 

It isn't a drop-in replacement for `datetime.strptime`, although they work similarly most of the time. 
Instead, think of it as of a library of its own. 

The full list of supported specifiers (`%Y`, `%m`, `%d`, ...) can be found in [chrono documentation](https://docs.rs/chrono/0.4.19/chrono/format/strftime/index.html).
They are a bit different from [Python's](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes).

## Notable differences from `datetime.strptime`

### Required parts of the template

`dtparse.parse` requires hours, minutes, and the full date to be present in the template.

For `datetime.strptime`, __all__ parts of the template are optional.

```python
datetime.strptime('2018/01/02 12', '%Y/%m/%d %H')  # no minutes in the template
# datetime(2018, 1, 2, 12, 0)

dtparse.parse('2018/01/02 12', '%Y/%m/%d %H')
# ValueError: input is not enough for unique date and time
```

### Specifiers for sub-second precision

Python uses `%f` as a specifier for microseconds, zero-padded on the left.
Chrono's `%f` is different - left-aligned, optionally zero-padded to the right.

```python
datetime.strptime('2004-12-01 13:02:47.123456', '%Y-%m-%d %H:%M:%S.%f')
# datetime(2004, 12, 1, 13, 2, 47, 123456)

dtparse.parse('2004-12-01 13:02:47.123456', '%Y-%m-%d %H:%M:%S.%f')
# datetime(2004, 12, 1, 13, 2, 47, 123)
```

On the other hand, Python's `.%f` works very close to chrono's `%.f`. 
The only difference is that chrono accepts up to 9 digits, because it parses
nanoseconds, not microseconds.

```python
datetime.strptime('2004-12-01 13:02:47.123456', '%Y-%m-%d %H:%M:%S.%f')
# datetime(2004, 12, 1, 13, 2, 47, 123456)

dtparse.parse('2004-12-01 13:02:47.123456', '%Y-%m-%d %H:%M:%S%.f')
# datetime(2004, 12, 1, 13, 2, 47, 123456)
```
```python
datetime.strptime('2004-12-01 13:02:47.123456789', '%Y-%m-%d %H:%M:%S.%f')
# ValueError: unconverted data remains: 789

dtparse.parse('2004-12-01 13:02:47.123456789', '%Y-%m-%d %H:%M:%S%.f')
# datetime(2004, 12, 1, 13, 2, 47, 123456)
```


##  How does it work?

Uses [chrono](https://github.com/chronotope/chrono) library under the cover.
Binds Rust to Python via [PyO3](https://github.com/PyO3/pyo3).
Wheels are built and distributed using GitHub actions, see the workflow 
[here](.github/workflows/ci.yml).

## Origins

This library was written for my talk on Rust extensions on [Yandex Pytup](https://events.yandex.ru/events/meetings/28-03-2018/).
It is intended to be both a stable library people can use, and a reference for those interested in 
extending Python with Rust.

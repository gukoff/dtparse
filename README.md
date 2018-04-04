# dtparse

A fast alternative to `datetime.strptime` written in Rust.
Uses [chrono](https://github.com/chronotope/chrono) under the cover. Binds Rust to Python via [PyO3](https://github.com/PyO3/pyo3).

It isn't fully compatible with `strptime` and requires hours and minutes to be present in the template.

This library is an example extension to my talk on Rust extensions on [Yandex Pytup](https://events.yandex.ru/events/meetings/28-03-2018/). 
You can use it as a template for your own extension. 
However, it works and is rather stable.

# usage
```python
from dtparse import parse

parse('2018/01/02 12:02:03', '%Y/%m/%d %H:%M:%S')  # datetime(2018, 1, 2, 12, 2, 3)
parse('2018/01/02 12:02', '%Y/%m/%d %H:%M')  # datetime(2018, 1, 2, 12, 2)
```

But:
```python
datetime.strptime('2018/01/02 12', '%Y/%m/%d %H')  # datetime(2018, 1, 2, 12, 0)
parse('2018/01/02 12', '%Y/%m/%d %H')  # ValueError: input is not enough for unique date and time
```

# distribution

There are two scripts to build wheels for this library.

`build_manylinux_wheels.sh` uses Docker to build [manylinux](https://github.com/pypa/manylinux) wheels for UNIX machines.

`build_osx_wheels.sh` is to be run locally on an OSX machine.

Result wheels can be found in the `dist/wheels` folder. They are ready to be uploaded to PYPI via the following command:
```bash
twine upload dist/wheels
```

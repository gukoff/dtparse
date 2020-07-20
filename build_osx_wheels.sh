#!/usr/bin/env bash
set -e

eval "$(pyenv init -)"

# This is an example of how the wheels can be built locally on OSX.
# It expects pyenv to be installed and the following virtualenvs to be created, e.g.:
# pyenv virtualenv 3.5.9 rust3.5
# pyenv virtualenv 3.6.10 rust3.6
# pyenv virtualenv 3.7.7 rust3.7
# pyenv virtualenv 3.8.2 rust3.8
# pyenv virtualenv 3.9-dev rust3.9

for venv in rust3.5 rust3.6 rust3.7 rust3.8 rust3.9; do
    pyenv activate "$venv"
    pip install -U pip setuptools setuptools-rust wheel delocate
    pip wheel . -w ./dist/wheels/
done

# Delocate is similar to auditwheel.
# If needed, it copies dynamic libraries into the wheel.
delocate-wheel -v ./dist/wheels/*macosx*.whl

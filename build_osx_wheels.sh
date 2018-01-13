#!/usr/bin/env bash
set -e

eval "$(pyenv init -)"

# This is an example of how the wheels can be built locally on OSX.
# It expects pyenv to be installed and the following virtualenvs to be created:
# pyenv virtualenv 2.7.14 rust2.7
# pyenv virtualenv 3.5.3 rust3.5
# pyenv virtualenv 3.6.3 rust3.6
# pyenv virtualenv 3.7-dev rust3.7

for venv in rust2.7 rust3.5 rust3.6 rust3.7; do
    pyenv activate "$venv"
    pip install -U pip setuptools setuptools-rust wheel delocate
    pip wheel . -w ./dist/wheels/
done

# Delocate is similar to auditwheel.
# If needed, it copies dynamic libraries into the wheel.
delocate-wheel -v ./dist/wheels/*macosx*.whl

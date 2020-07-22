#!/usr/bin/env bash

curl https://sh.rustup.rs -sSf | bash -s -- -y
source $HOME/.cargo/env
pip install setuptools-rust

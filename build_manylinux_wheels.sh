#!/usr/bin/env bash
set -e

# We use Dockerfile to make use of caching and to not reinstall rustc for every build.
# In case you'd like to use a newer version of rustc, you can use `docker build --no-cache` here.
docker build -f ./dist/manylinux/Dockerfile -t manylinux_rust .
docker run --rm -v `pwd`/dist/wheels:/app/dist/wheels manylinux_rust

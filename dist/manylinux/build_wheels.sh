#!/bin/sh
set -e -x

export PATH="$HOME/rust/bin:$PATH"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$HOME/rust/lib"

mkdir /tmp/wheels

# Compile wheels
for PYBIN in /opt/python/cp35-cp35m/bin; do
    export PYTHON_LIB=$(${PYBIN}/python -c "import sysconfig; print(sysconfig.get_config_var('LIBDIR'))")
    export LIBRARY_PATH="$LIBRARY_PATH:$PYTHON_LIB"
    export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$PYTHON_LIB"

    "${PYBIN}/pip" install -U setuptools setuptools-rust wheel
    "${PYBIN}/pip" wheel /app/ -w /tmp/wheels
done

# `auditwheel repair` copies the external shared libraries into the wheel itself
# and automatically modifies the appropriate RPATH entries such that these libraries
# will be picked up at runtime. This accomplishes a similar result as if the libraries
# had been statically linked without requiring changes to the build system.
for whl in /tmp/wheels/*; do
    auditwheel repair "$whl" -w /app/dist/wheels
done

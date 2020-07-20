#!/bin/sh
set -e -x

export PATH="$HOME/.cargo/bin:$PATH"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$HOME/rust/lib"

WHEELS_TMP_DIR=/tmp/wheels


# Compile wheels
for PYBIN in /opt/python/cp{35,36,37,38,39}*/bin; do
    export PYTHON_SYS_EXECUTABLE="$PYBIN/python"
    export PYTHON_LIB=$("${PYBIN}/python" -c "import sysconfig; print(sysconfig.get_config_var('LIBDIR'))")
    export LIBRARY_PATH="$LIBRARY_PATH:$PYTHON_LIB"
    export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$PYTHON_LIB"

    "${PYBIN}/pip" install -U setuptools setuptools-rust wheel

    # `auditwheel repair` copies the external shared libraries into the wheel itself
    # and automatically modifies the appropriate RPATH entries such that these libraries
    # will be picked up at runtime. This accomplishes a similar result as if the libraries
    # had been statically linked without requiring changes to the build system.
    mkdir $WHEELS_TMP_DIR
    "${PYBIN}/pip" wheel /app/ -w $WHEELS_TMP_DIR
    for whl in $WHEELS_TMP_DIR/*; do
        auditwheel repair "$whl" -w /app/dist/wheels
    done
    rm -rf $WHEELS_TMP_DIR
done

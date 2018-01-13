FROM quay.io/pypa/manylinux1_x86_64

RUN mkdir ~/rust-installer
RUN curl -sL https://static.rust-lang.org/rustup.sh -o ~/rust-installer/rustup.sh
RUN sh ~/rust-installer/rustup.sh --prefix=~/rust --channel=nightly -y --disable-sudo
COPY . /app

ENTRYPOINT /app/dist/manylinux/build_wheels.sh

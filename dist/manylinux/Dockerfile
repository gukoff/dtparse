FROM quay.io/pypa/manylinux2010_x86_64

RUN mkdir ~/rust-installer

RUN curl https://sh.rustup.rs -sSf | bash -s -- -y
RUN echo "source $HOME/.cargo/env" >> "$HOME/.bashrc"
RUN echo "source $HOME/.cargo/env" >> "$HOME/.bash_profile"

COPY . /app

ENTRYPOINT /app/dist/manylinux/build_wheels.sh

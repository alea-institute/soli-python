FROM ubuntu:24.04

# define package version
ARG SOLI_VERSION=0.1.5

# Avoid prompts from apt
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-venv \
    curl

# create /app directory
WORKDIR /app
RUN cd /app

# create a virtual environment
RUN python3 -m venv /app/.venv

# install pytest into it
RUN /app/.venv/bin/pip install pytest pytest-benchmark

# copy the SOLI_VERSION wheel:
COPY dist/soli_python-${SOLI_VERSION}-py3-none-any.whl /app/

# install the wheels with extra 'search'
RUN /app/.venv/bin/pip install /app/soli_python-${SOLI_VERSION}-py3-none-any.whl[search]

# copy the tests directory
COPY tests /app/tests

# run the tests
CMD ["/app/.venv/bin/pytest", "/app/tests"]

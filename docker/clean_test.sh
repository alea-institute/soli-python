#!/usr/bin/env bash
# This script is used to test a clean install and tests for
# the built wheel images.

# Build the wheel
poetry build \
  && \
  docker build -t soli-python-ubuntu2404-install -f docker/ubuntu2404-install/Dockerfile . \
  && \
  docker run soli-python-ubuntu2404-install:latest

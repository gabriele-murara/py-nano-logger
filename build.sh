#! /bin/bash

rm -rf nano_logger.egg-info
rm -rf dist
python -m pip install --upgrade setuptools wheel build
python -m build

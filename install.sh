#!/bin/bash
python -m venv .venv && \
. .venv/bin/activate && \

pip install flask-restful  && \
pip install api.py && \
pip install gunicorn

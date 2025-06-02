#!/bin/bash
python3 -m venv .venv && \
. .venv/bin/activate && \

pip install flask-restful  && \
pip install api.py && \
pip install gunicorn

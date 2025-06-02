#/bin/bash
BIND_ADDRESS="$1"
if [ ! -d ".venv" ]; then
  ./install.sh
fi
gunicorn -w 1 -b '$1' 'api:app'
#!/bin/sh
export PODMAN01_FLAG="$(cat /opt/ctf/.flag-env 2>/dev/null)"
exec python app.py

#!/bin/bash

set -e

echo "--- [DIAGNOSTIC] Starting run.sh script ---"
echo "--- [DIAGNOSTIC] Current directory is: $(pwd) ---"
echo "--- [DIAGNOSTIC] Listing files in current directory: ---"
ls -la
echo "--- [DIAGNOSTIC] --- End of file list ---"

echo "--- [ACTION] Forcibly setting PYTHONPATH to ensure modules are found ---"
export PYTHONPATH=/opt/render/project/src

echo "--- [ACTION] Starting Gunicorn server with CORRECT project name... ---"
# السطر التالي هو الذي تم تصحيحه
exec gunicorn myproject.wsgi:application --bind 0.0.0.0:$PORT --log-level=debug
#!/bin/bash

# هذا السطر يضمن أن السكربت سيتوقف فورًا إذا فشل أي أمر
set -e

# --- قسم التشخيص ---
echo "--- [DIAGNOSTIC] Starting run.sh script ---"
echo "--- [DIAGNOSTIC] Current directory is: $(pwd) ---"
echo "--- [DIAGNOSTIC] Listing files in current directory: ---"
ls -la
echo "--- [DIAGNOSTIC] --- End of file list ---"

# --- قسم التنفيذ ---
echo "--- [ACTION] Forcibly setting PYTHONPATH to ensure modules are found ---"
# هذا الأمر يجبر بايثون على البحث في المجلد الصحيح
export PYTHONPATH=/opt/render/project/src

echo "--- [ACTION] Starting Gunicorn server... ---"
# هذا هو أمر التشغيل النهائي مع تسجيل مفصل للأخطاء
exec gunicorn qssunreports.wsgi:application --bind 0.0.0.0:$PORT --log-level=debug
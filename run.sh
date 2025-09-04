#!/bin/bash

# هذا السطر يضمن أن السكربت سيتوقف فورًا إذا فشل أي أمر
set -e

# هذا هو السطر الأهم: يخبر بايثون أن يضيف المجلد الحالي إلى مسار البحث
# $(pwd) سيتم استبدالها تلقائيًا بالمسار الصحيح على خادم Render
export PYTHONPATH=$PYTHONPATH:$(pwd)

# أخيرًا، قم بتشغيل خادم gunicorn
gunicorn qssunreports.wsgi:application
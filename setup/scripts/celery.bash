#!/bin/bash

if [[ "${1}" == "celery" ]]; then
  celery -A app.tasks.celery_app:worker worker -l INFO
elif [[ "${1}" == "flower" ]]; then
  celery -A app.tasks.celery_app:worker flower
elif [[ "${1}" == "beat" ]]; then
  celery -A app.tasks.celery_app:worker worker -l INFO -B
fi


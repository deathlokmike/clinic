#!/bin/bash

alembic upgrade head

python setup/scripts/init_db.py

gunicorn app.main:app --workers 5 --worker-class app.custom_uvicorn.CustomUvicornWorker --bind=0.0.0.0:8000
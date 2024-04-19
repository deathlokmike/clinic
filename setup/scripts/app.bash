#!/bin/bash

alembic upgrade head

python setup/scripts/init_db.py

gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000

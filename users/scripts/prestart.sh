#! /usr/bin/env bash

python3 /app/scripts/wait_database.py

alembic upgrade head

python3 /app/scripts/initial_data.py

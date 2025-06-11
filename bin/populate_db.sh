#!/bin/sh
# run the database populate script
cd "$(dirname "$0")/../server" || exit 1
python3 src/populate_database.py

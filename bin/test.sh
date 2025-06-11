#!/bin/sh
# Run Tests
cd "$(dirname "$0")/.." || exit 1
PYTHONPATH=server/src pytest server/src/test_main.py

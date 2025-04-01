#!/bin/bash
export PYTHONPATH=$(pwd)
python src/weather.py
python src/find_my_flight.py
git add .
git commit -m "Auto-update via manual_fetch.sh"
git push
#!/bin/bash
export PYTHONPATH=$(pwd)
python src/weather.py
python src/utils/get_flight_prices.py
git add .
git commit -m "Auto-update via manual_fetch.sh"
git push
import os
from datetime import datetime
from src.weather import get_weather

def test_file_creation():
    today = datetime.today().strftime('%Y-%m-%d')
    new_directory = f'./data/{today}'
    weather_file_path = new_directory + '/temps.csv'
    assert os.path.exists(weather_file_path)
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(city):
    openweather_api_key = os.getenv("OPENWEATHER_API_KEY")
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweather_api_key}"

    response = requests.get(url)
    data = response.json()
    kelvin_temp = data['main']['temp_max']
    temp = round(kelvin_temp - 273)
    return temp

if __name__ == "__main__":
    print(get_weather('Tripoli'))
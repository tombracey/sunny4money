from datetime import datetime
import csv
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(city):
    openweather_api_key = os.getenv("OPENWEATHER_API_KEY")
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweather_api_key}"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        kelvin_temp = data['main']['temp_max']
        temp = round(kelvin_temp - 273)
        return temp
    else:
        return None

locations = {
    "UK": {"city": "London", "country": "UK"},
    "CDG": {"city": "Paris", "country": "France"},
    "AMS": {"city": "Amsterdam", "country": "Netherlands"},
    "FCO": {"city": "Rome", "country": "Italy"},
    "MAD": {"city": "Madrid", "country": "Spain"},
    "LIS": {"city": "Lisbon", "country": "Portugal"},
    "ATH": {"city": "Athens", "country": "Greece"},
    "BCN": {"city": "Barcelona", "country": "Spain"},
    "BER": {"city": "Berlin", "country": "Germany"},
    "MXP": {"city": "Milan", "country": "Italy"},
    "VIE": {"city": "Vienna", "country": "Austria"},
    "BRU": {"city": "Brussels", "country": "Belgium"},
    "PRG": {"city": "Prague", "country": "Czech Republic"},
    "BUD": {"city": "Budapest", "country": "Hungary"},
    "ZRH": {"city": "Zurich", "country": "Switzerland"},
    "CAI": {"city": "Cairo", "country": "Egypt"},
    "CMN": {"city": "Casablanca", "country": "Morocco"},
    "RAK": {"city": "Marrakech", "country": "Morocco"},
    "TUN": {"city": "Tunis", "country": "Tunisia"},
    "ALG": {"city": "Algiers", "country": "Algeria"},
    "TIP": {"city": "Tripoli", "country": "Libya"},
    "TNG": {"city": "Tangier", "country": "Morocco"},
    "BEY": {"city": "Beirut", "country": "Lebanon"},
    "AMM": {"city": "Amman", "country": "Jordan"},
    "IST": {"city": "Istanbul", "country": "Turkey"},
    "DOH": {"city": "Doha", "country": "Qatar"},
    "BAH": {"city": "Manama", "country": "Bahrain"}
}

headers = ["City", "Temperature (°C)"]

today = datetime.today().strftime('%Y-%m-%d')
new_directory = f'./data/{today}'
os.makedirs(new_directory, exist_ok=True)

weather_file_path = new_directory + '/temps.csv'
with open(weather_file_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)

    for code, details in locations.items():
        city = details["city"]
        temp = get_weather(city)
        
        if temp:
            writer.writerow([city, temp])
from datetime import datetime
import csv
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(city):
    openweather_api_key = os.getenv("OPENWEATHER_API_KEY")
    
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={openweather_api_key}"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        max_kelvin_temp = 0
        
        for forecast in data['list']:
            kelvin_temp = forecast['main']['temp_max']
            
            if max_kelvin_temp is None or kelvin_temp > max_kelvin_temp:
                max_kelvin_temp = kelvin_temp
        
        temp = round(max_kelvin_temp - 273)
        return temp
    else:
        return None


locations = {
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
    "BAH": {"city": "Manama", "country": "Bahrain"},
    "NCE": {"city": "Nice", "country": "France"},
    "JTR": {"city": "Santorini", "country": "Greece"},
    "FAO": {"city": "Albufeira", "country": "Portugal"},
    "CTA": {"city": "Catania", "country": "Italy"},
    "AGP": {"city": "Malaga", "country": "Spain"},
    "DBV": {"city": "Dubrovnik", "country": "Croatia"},
    "NAP": {"city": "Naples", "country": "Italy"},
    "TLN": {"city": "Toulon", "country": "France"},
    "SSH": {"city": "Sharm El Sheikh", "country": "Egypt"},
    "HRG": {"city": "Hurghada", "country": "Egypt"},
    "DJE": {"city": "Djerba", "country": "Tunisia"},
    "ESU": {"city": "Essaouira", "country": "Morocco"},
    "AGA": {"city": "Agadir", "country": "Morocco"}
}


today = datetime.today().strftime('%Y-%m-%d')
new_directory = f'./data/{today}'
os.makedirs(new_directory, exist_ok=True)

weather_file_path = new_directory + '/temps.csv'
with open(weather_file_path, 'w', newline='') as f:
    headers = ["City", "Temperature (°C)"]
    writer = csv.writer(f)
    writer.writerow(headers)

    uk = "United Kingdom"
    uk_temp = get_weather(uk)
    writer.writerow([uk, uk_temp])

    for code, details in locations.items():
        city = details["city"]
        temp = get_weather(city)
        
        if temp > uk_temp:
            writer.writerow([city, temp])

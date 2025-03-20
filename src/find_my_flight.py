import os
import csv
import math
from datetime import datetime
import pandas as pd
from src.utils.get_flight_price import get_min_flight_price
from src.utils.find_nearest_airport import find_nearest_airport
from src.utils.gemini import gemini

destinations = {
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

def find_my_flight(location: str, budget):
    departure_code = find_nearest_airport(location)[0]

    today = datetime.today().strftime('%Y-%m-%d')
    new_directory = f'./data/{today}'
    if not os.path.exists(new_directory):
        os.makedirs(new_directory, exist_ok=True)

    dir_path = f'./data/{today}'
    csv_path = dir_path + f'/{departure_code}.csv'

    if not os.path.exists(csv_path):
        headers = ["City", "Price", "Date"]
        with open (csv_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            for destination, details in destinations.items():
                flight = get_min_flight_price(departure_code, destination)
                if flight:
                    city = details["city"]
                    price = flight[0]
                    date = flight[1]
                    writer.writerow([city, price, date])
    temps_df = pd.read_csv(f'{dir_path}/temps.csv')
    flights_df = pd.read_csv(csv_path)
    merged_df = pd.merge(flights_df, temps_df, on="City", how="inner")
    london_temp = temps_df.loc[temps_df['City'] == 'London', 'Temperature (°C)'].values[0]
    filtered_df = merged_df[(merged_df['Price'] <= budget) & (merged_df['Temperature (°C)'] > london_temp)]

    if filtered_df.empty:
        return None

    hottest_city_row = filtered_df.loc[filtered_df['Temperature (°C)'].idxmax()]
    city_name = hottest_city_row['City']
    temperature = int(hottest_city_row['Temperature (°C)'])
    flight_price = float(hottest_city_row['Price'])
    uk_temp_diff = temperature - int(temps_df[temps_df['City'] == "London"]['Temperature (°C)'].values[0])

    unformatted_date = hottest_city_row['Date']
    flight_date = datetime.strptime(unformatted_date, "%Y-%m-%d").strftime("%d %B %Y")

    ai_overview = gemini(f'Write a couple paragraphs to someone who is going to {city_name} with plane tickets costing £{flight_price}. It is {uk_temp_diff} hotter than here in the UK. Talk about what a great destination it is, how they are getting a lot of sun for value and the unique attractions/history/culture. No preamble.')

    depart_from = find_nearest_airport(location)[1]
    pic_path = f'media/images/{city_name}.jpg'

    return depart_from, city_name, pic_path, flight_price, flight_date, temperature, uk_temp_diff, ai_overview

print(find_my_flight("Hanwell", 45))
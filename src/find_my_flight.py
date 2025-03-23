import os
import csv
import math
from datetime import datetime
import pandas as pd
from src.utils.get_flight_price import get_min_flight_price
from src.utils.find_nearest_airport import find_nearest_airport
from src.utils.gemini import gemini

destinations = {
    "CDG": {"city": "Paris", "country": "France", "beach": False},
    "AMS": {"city": "Amsterdam", "country": "Netherlands", "beach": False},
    "FCO": {"city": "Rome", "country": "Italy", "beach": True},
    "MAD": {"city": "Madrid", "country": "Spain", "beach": False},
    "LIS": {"city": "Lisbon", "country": "Portugal", "beach": True},
    "ATH": {"city": "Athens", "country": "Greece", "beach": True},
    "BCN": {"city": "Barcelona", "country": "Spain", "beach": True},
    "BER": {"city": "Berlin", "country": "Germany", "beach": False},
    "MXP": {"city": "Milan", "country": "Italy", "beach": False},
    "VIE": {"city": "Vienna", "country": "Austria", "beach": False},
    "BRU": {"city": "Brussels", "country": "Belgium", "beach": False},
    "PRG": {"city": "Prague", "country": "Czech Republic", "beach": False},
    "BUD": {"city": "Budapest", "country": "Hungary", "beach": False},
    "ZRH": {"city": "Zurich", "country": "Switzerland", "beach": False},
    "CAI": {"city": "Cairo", "country": "Egypt", "beach": False},
    "CMN": {"city": "Casablanca", "country": "Morocco", "beach": True},
    "RAK": {"city": "Marrakech", "country": "Morocco", "beach": False},
    "TUN": {"city": "Tunis", "country": "Tunisia", "beach": True},
    "ALG": {"city": "Algiers", "country": "Algeria", "beach": True},
    "TIP": {"city": "Tripoli", "country": "Libya", "beach": True},
    "TNG": {"city": "Tangier", "country": "Morocco", "beach": True},
    "BEY": {"city": "Beirut", "country": "Lebanon", "beach": True},
    "AMM": {"city": "Amman", "country": "Jordan", "beach": True},
    "IST": {"city": "Istanbul", "country": "Turkey", "beach": True},
    "DOH": {"city": "Doha", "country": "Qatar", "beach": True},
    "BAH": {"city": "Manama", "country": "Bahrain", "beach": True},
    "NCE": {"city": "Nice", "country": "France", "beach": True},
    "JTR": {"city": "Santorini", "country": "Greece", "beach": True},
    "FAO": {"city": "Albufeira", "country": "Portugal", "beach": True},
    "CTA": {"city": "Catania", "country": "Italy", "beach": True},
    "AGP": {"city": "Malaga", "country": "Spain", "beach": True},
    "DBV": {"city": "Dubrovnik", "country": "Croatia", "beach": True},
    "NAP": {"city": "Naples", "country": "Italy", "beach": True},
    "TLN": {"city": "Toulon", "country": "France", "beach": True},
    "SSH": {"city": "Sharm El Sheikh", "country": "Egypt", "beach": True},
    "HRG": {"city": "Hurghada", "country": "Egypt", "beach": True},
    "DJE": {"city": "Djerba", "country": "Tunisia", "beach": True},
    "ESU": {"city": "Essaouira", "country": "Morocco", "beach": True},
    "AGA": {"city": "Agadir", "country": "Morocco", "beach": True}
}

def find_my_flight(location: str, budget, see_the_sea=False):
    departure_code = find_nearest_airport(location)[0]

    today = datetime.today().strftime('%Y-%m-%d')
    new_directory = f'./data/{today}'
    if not os.path.exists(new_directory):
        os.makedirs(new_directory, exist_ok=True)

    dir_path = f'./data/{today}'
    csv_path = dir_path + f'/{departure_code}.csv'

    headers = ["City", "Price", "Date", "Beach"]
    with open (csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for destination, details in destinations.items():
            flight = get_min_flight_price(departure_code, destination)
            if flight:
                city = details["city"]
                beach = details["beach"]
                price = flight[0]
                date = flight[1]
                writer.writerow([city, price, date, beach])
    temps_df = pd.read_csv(f'{dir_path}/temps.csv')
    flights_df = pd.read_csv(csv_path)
    merged_df = pd.merge(flights_df, temps_df, on="City", how="inner")
    uk_avg_temp = int(temps_df.loc[temps_df['City'] == 'United Kingdom', 'Temperature (°C)'].values[0])
    filtered_df = merged_df[merged_df['Price'] <= budget]

    if see_the_sea:
        filtered_df = filtered_df[filtered_df['Beach'] == True]

    if filtered_df.empty:
        return None

    hottest_city_row = filtered_df.loc[filtered_df['Temperature (°C)'].idxmax()]
    city_name = hottest_city_row['City']
    temperature = int(hottest_city_row['Temperature (°C)'])
    flight_price = float(hottest_city_row['Price'])

    unformatted_date = hottest_city_row['Date']
    flight_date = datetime.strptime(unformatted_date, "%Y-%m-%d").strftime("%d %B %Y")

    ai_overview = gemini(f'Write 2 couple paragraphs split by <<PARAGRAPH>> to someone who is going to {city_name} with plane tickets costing £{flight_price}. It is {temperature-uk_avg_temp} hotter than here in the UK. Talk about what a great destination it is, how they are getting a lot of sun for value and the unique attractions/history/culture. No preamble.')
    ai_para_1 = ai_overview[0]
    ai_para_2 = ai_overview[1]

    depart_from = find_nearest_airport(location)[1]
    pic_path = f'media/images/{city_name}.jpg'

    return depart_from, city_name, pic_path, flight_price, flight_date, temperature, uk_avg_temp, ai_para_1, ai_para_2

print(find_my_flight("Hanwell", 45))
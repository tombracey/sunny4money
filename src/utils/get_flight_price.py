import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

def get_min_flight_price(departure_id, destination_id):
    rapid_api_key = os.getenv("RAPIDAPI_KEY")

    today = datetime.today().strftime('%Y-%m-%d')

    url = "https://booking-com15.p.rapidapi.com/api/v1/flights/getMinPrice"

    querystring = {
        "fromId": f"{departure_id}.AIRPORT",
        "toId": f"{destination_id}.AIRPORT",
        "departDate": today,
        "cabinClass": "ECONOMY",
        "currency_code": "GBP",
        "sort": "CHEAPEST"
    }

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "booking-com15.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        print("Raw response text:", response.text)
        return None

    cheapest_flight = None
    if "data" in data:
        for flight in data["data"]:
            if cheapest_flight is None or flight["price"]["units"] < cheapest_flight["price"]["units"]:
                cheapest_flight = flight

    if cheapest_flight:
        price_units = cheapest_flight["price"]["units"]
        price_nanos = cheapest_flight["price"]["nanos"]
        price = price_units + price_nanos / 1e9
        date = cheapest_flight['departureDate']
        return price, date
    else:
        return None

if __name__ == "__main__":
    print(get_min_flight_price("LON", "PAR"))
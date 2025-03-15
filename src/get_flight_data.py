import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RAPIDAPI_KEY")

url = "https://booking-com15.p.rapidapi.com/api/v1/flights/getMinPrice"

querystring = {
    "fromId": "LON.AIRPORT",
    "toId": "PAR.AIRPORT",
    "departDate": "2025-03-20",
    "cabinClass": "ECONOMY",
    "currency_code": "GBP",
    "sort": "CHEAPEST"
}

headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "booking-com15.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()

cheapest_flight = None
if "data" in data:
    for flight in data["data"]:
        if cheapest_flight is None or flight["price"]["units"] < cheapest_flight["price"]["units"]:
            cheapest_flight = flight

if cheapest_flight:
    price_units = cheapest_flight["price"]["units"]
    price_nanos = cheapest_flight["price"]["nanos"]
    total_price = price_units + price_nanos / 1e9
    print(f"Cheapest flight: £{total_price:.2f} on {cheapest_flight['departureDate']}")
else:
    print("No flights found")

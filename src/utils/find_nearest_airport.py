from src.utils.geocode_address import geocode_address
import math

def find_nearest_airport(location: str):

    uk_airports = {
        "LON": {"name": "London", "coords": [51.5958, -0.1949]},  # Average coords of London airports
        "MAN": {"name": "Manchester Airport", "coords": [53.3650, -2.272]},
        "EDI": {"name": "Edinburgh Airport", "coords": [55.9500, -3.3725]},
        "BHX": {"name": "Birmingham Airport", "coords": [52.4520, -1.7480]},
        "BRS": {"name": "Bristol Airport", "coords": [51.3827, -2.7191]},
        "GLA": {"name": "Glasgow Airport", "coords": [55.8719, -4.4331]},
        "LPL": {"name": "Liverpool John Lennon Airport", "coords": [53.3331, -2.8497]}
    }

    def find_relative_distance(airport_code, airport_coords, user_coords):
        lat1, lon1 = airport_coords
        lat2, lon2 = user_coords
        
        lat_diff = lat2 - lat1
        lon_diff = lon2 - lon1
        
        distance = math.sqrt(lat_diff**2 + lon_diff**2)
        
        return airport_code, distance

    user_coords = geocode_address(location)

    distances = {}

    for airport, details in uk_airports.items():
        airport_code = airport
        aiport_name = details["name"]
        airport_coords = details["coords"]
        airport_code, distance = find_relative_distance(airport_code, airport_coords, user_coords)
        distances[airport_code] = distance

    departure_code = min(distances, key=distances.get)
    airport_name = uk_airports[departure_code]["name"]

    return departure_code, airport_name

if __name__ == "__main__":
    print(find_nearest_airport("Salford, Manchester"))

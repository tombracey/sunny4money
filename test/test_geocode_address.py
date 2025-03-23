import pytest
from src.utils.geocode_address import geocode_address

def test_geocoding_of_postcode_input():
    input = "SW1A 2AA"
    expected_lat, expected_lon = 51.5034, -0.1276
    lat, lon = geocode_address(input)

    assert lat == pytest.approx(expected_lat, abs=0.001)
    assert lon == pytest.approx(expected_lon, abs=0.001)

def test_geocoding_of_city_input():
    input = "London"

    lat_min = 51.30
    lat_max = 51.70
    lon_min = -0.53
    lon_max = 0.33

    coords = geocode_address(input)
    lat = coords[0]
    lon = coords[1]
    assert lat_min <= lat <= lat_max
    assert lon_min <= lon <= lon_max


import pytest
from unittest.mock import patch, MagicMock
from src.utils.get_flight_price import get_min_flight_price

def test_gets_the_minimum_flight_price():
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "data": [
            {
                "price": {
                    "units": 50,
                    "nanos": 500000000
                },
                "departureDate": "2025-03-24T12:00:00"
            },
            {
                "price": {
                    "units": 60,
                    "nanos": 0
                },
                "departureDate": "2025-03-25T12:00:00"
            }
        ]
    }
    with patch('requests.get', return_value=mock_response):
        departure_id = "LON"
        destination_id = "PAR"
        price, date = get_min_flight_price(departure_id, destination_id)

    assert price == 50.50
    assert date == "2025-03-24T12:00:00"
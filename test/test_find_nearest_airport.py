from src.utils.find_nearest_airport import find_nearest_airport

def test_postcode_input():
    input = "SW1A 2AA"
    expected = ("LON", "London")
    assert find_nearest_airport(input) == expected

def test_for_scottish_locations():
    location_inputs = ["Glasgow Central", "Hebrides", "Aberdeen Railway Station"]
    expected_results = [("GLA", "Glasgow Airport"), ("EDI", "Edinburgh Airport")]

    for location in location_inputs:
        result = find_nearest_airport(location)
        assert result in expected_results
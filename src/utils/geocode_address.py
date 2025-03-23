import boto3

client = boto3.client('location')

def geocode_address(address):
        location = address + ", United Kingdom"
        response = client.search_place_index_for_text(
            IndexName='MyPlaceIndex',
            Text=location
        )
        lon, lat = response['Results'][0]['Place']['Geometry']['Point']
        coordinates = (lat, lon)
        return coordinates

print(geocode_address("Hanwell"))
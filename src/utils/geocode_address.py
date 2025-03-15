import boto3

client = boto3.client('location')

def geocode_address(address):
        response = client.search_place_index_for_text(
            IndexName='MyPlaceIndex',
            Text=address
        )
        coordinates = response['Results'][0]['Place']['Geometry']['Point']
        return coordinates

if __name__ == "__main__":
    print(geocode_address("Ealing"))
    print(geocode_address("Glasgow"))
    print(geocode_address("SW19"))

import requests

def main():   
	URL = "http://maps.googleapis.com/maps/api/geocode/json"

	location = raw_input('Enter an address: ')
	
	print("Searching: %s"
	      %(location))

	PARAMS = {'address':location}

	r = requests.get(url = URL, params = PARAMS)

	data = r.json()

	latitude = data['results'][0]['geometry']['location']['lat']
	longitude = data['results'][0]['geometry']['location']['lng']
	formatted_address = data['results'][0]['formatted_address']
	
	print("************************")
	print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
	      %(latitude, longitude,formatted_address))
	print("************************")

   	return;



import folium
from geopy.geocoders import Nominatim

# Read the team member locations from the file
with open('locations.txt', 'r') as file:
    team_locations = [line.strip() for line in file.readlines()]

# Create the map
map = folium.Map(location=[51.1657, 10.4515], zoom_start=6)

# Geocode and add markers for each team member's location
geolocator = Nominatim(user_agent="my_team_map")
for location in team_locations:
    try:
        name, city = location.split(', ')
        address = f"{name}, {city}"
        loc = geolocator.geocode(city, country_codes="de", exactly_one=False, featuretype="city")[0]
        if loc is not None:
            marker = folium.Marker(location=[loc.latitude, loc.longitude], popup=address)
            marker.add_to(map)
        else:
            print(f"Failed to geocode location: {location}. No result found.")
    except Exception as e:
        print(f"Failed to geocode location: {location}. Error: {str(e)}")

# Save the map to an HTML file
map.save('team_map.html')


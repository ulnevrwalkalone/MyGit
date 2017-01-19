import requests
my_location= "401 North front Street Columbus Ohio"

def location(my_location):
    list_location= my_location.split()
    api_location= '+'.join(map(str, list_location))
    geo_url='https://maps.googleapis.com/maps/api/geocode/json?address='+str(api_location)+'&key=AIzaSyBWd4YTG2hiHRgyv16kql8GMpEKX-3kRzk'
    g=requests.get(geo_url)
    geo_dict = g.json()
    results_list=geo_dict['results']
    print(results_list)

#Need to figure out how to pull dictionary out of a list from a dictionary

location(my_location)

"""
geometry_dict=geo_dict['geometry']
location_dict = geometry_dict['location']
latitude=location_dict['lat']
longitude=location_dict['lng']
print(str(latitude)+','+str(longitude))
"""

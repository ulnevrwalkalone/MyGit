import requests
my_location= ""
latitude='1'
longitude='2'

def location(my_location):
    my_location=input('Please enter your location: ')
    list_location= my_location.split()
    api_location= '+'.join(map(str, list_location))
    geo_url='https://maps.googleapis.com/maps/api/geocode/json?address='+str(api_location)+'&key=AIzaSyBWd4YTG2hiHRgyv16kql8GMpEKX-3kRzk'
    g=requests.get(geo_url)
    geo_dict = g.json()
    global latitude
    global longitude
    latitude=geo_dict['results'][0]['geometry']['location']['lat']
    longitude=geo_dict['results'][0]['geometry']['location']['lng']
    return(latitude,longitude)

#location(my_location)

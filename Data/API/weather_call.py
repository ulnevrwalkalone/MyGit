import requests
my_location=input('Please enter your location: ')
latitude='1'
longitude='2'
temperature= '00'

def location(my_location):
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
location(my_location)

def dark_sky(latitude, longitude):
    #make an API call and store the response
    url= 'https://api.darksky.net/forecast/f093cde891c1e796d5917d07cdc2c0d0/%s,%s' %(latitude, longitude)
    r= requests.get(url)

    #store api response in a variable
    response_dict = r.json()
    global temperature
    temperature=response_dict['currently']['temperature']
    #Proces results
    return(str(temperature))

dark_sky(latitude,longitude)

print('The current temperature for %s is %s degrees fehrenheit' %(my_location, temperature))

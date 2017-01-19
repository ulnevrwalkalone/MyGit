import requests, os, datetime

my_location= input("Please enter your location")
api_location=''

def location(my_location):
    list_location= my_location.split()
    api_location= '+'.join(map(str, list_location))

location(my_location)

geo_url='https://maps.googleapis.com/maps/api/geocode/json?address='+str(api_location)+'&key=AIzaSyBWd4YTG2hiHRgyv16kql8GMpEKX-3kRzk'
g=requests.get(geo_url)
geo_dict = g.json()
location_dict = geo_dict['location']
latitude=location_dict['lat']
longitude=location_dict['lng']
#make an API call and store the response
url= 'https://api.darksky.net/forecast/f093cde891c1e796d5917d07cdc2c0d0/'+str(latitude)+','+str(longitude)
#+latitude+','+longitude'
r= requests.get(url)

#store api response in a variable
response_dict = r.json()
currently_dict=response_dict['currently']

#Proces results
print(currently_dict.keys())

"""print("Timezone :", response_dict['timezone'])
print("Current Time :", currently_dict['time'] )
print(currently_dict['cloudCover'])"""

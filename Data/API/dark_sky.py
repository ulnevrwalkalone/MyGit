import requests, os, datetime
from location import location, my_location, latitude, longitude

def dark_sky(latitude, longitude):
    #make an API call and store the response
    url= 'https://api.darksky.net/forecast/f093cde891c1e796d5917d07cdc2c0d0/%s,%s' %(latitude, longitude)
    r= requests.get(url)

    #store api response in a variable
    response_dict = r.json()
    currently_dict=response_dict['currently']['temperature']
    global my_location
    #Proces results
    return(str(currently_dict))


location(my_location)
dark_sky(latitude, longitude)

print('The current temperature for %s is %s' %(my_location, currently_dict))

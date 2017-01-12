import requests, os, datetime

latitude=40.010379
longitude=-82.991084
#make an API call and store the response
url= 'https://api.darksky.net/forecast/f093cde891c1e796d5917d07cdc2c0d0/40.010379,-82.991084'
#+latitude+','+longitude'
r= requests.get(url)

#store api response in a variable
response_dict = r.json()
currently_dict=response_dict['currently']
print("Timezone :", response_dict['timezone'])
print("Current Time :", currently_dict['time'] )

#Proces results
#print(response_dict.keys())

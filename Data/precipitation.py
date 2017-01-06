import csv
from matplotlib import pyplot as plt
from datetime import datetime

#get rainfall and snowfall from file
filename= r'C:\Users\wrussell\Documents\GitHub\MyGit\Data\winter16.csv'
with open(filename) as f:
    reader= csv.reader(f)
    header_row = next(reader)

    rainfall, snowfall=[],[]
    for row in reader:
        precip=row[19]
        event= row[21]
        if float(precip) >0:
            if event== 'Snow':
                snow=float(row[19])
                snowfall.append(snow)
            else:
                rain=float(row[19])
                rainfall.append(rain)
        else:
            continue

    total_snowfall=sum(snowfall)
    total_rainfall=sum(rainfall)
    print("The toal snowfall was: " +str(total_snowfall) +" and the total rainfall was: "+str(total_rainfall))

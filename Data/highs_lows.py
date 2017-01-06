import csv
from matplotlib import pyplot as plt
from datetime import datetime

#get dates & high temps from file
filename= r'C:\Users\wrussell\Documents\GitHub\MyGit\Data\sitka_weather_01-2014.csv'
with open(filename) as f:
    reader= csv.reader(f)
    header_row = next(reader)

    dates, highs=[], []
    for row in reader:
        current_date= datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high=int(row[1])
        highs.append(high)


#Plot data
fig= plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red')

#format Plot
plt.title("Daily high temperatures, January 2014", fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

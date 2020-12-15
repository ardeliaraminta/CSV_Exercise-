import csv
import statistics
from statistics import mean 
from statistics import median
import numpy as np 
import matplotlib.pyplot as plt 

"""load csv file and ignored missing data or NA """

with open('activity.csv','r')as f:
    data = csv.reader(f)
    mydictionary = {}
    for row in data:
        if row[0] != '0' and row[1] != 'date' and row [0] != 'NA':
            if row[1] not in mydictionary:
                mydictionary[row[1]] = [int(row[0])]
            else:
                mydictionary[row[1]].append(int(row[0]))

total_per_day = {}
mean_total_per_day ={}
median_per_day = {}
for key, value in mydictionary.items():
    total_per_day[key] = sum(value)
    mean_total_per_day[key] = round(mean(value),2)
    median_per_day[key] = median(value)

print(total_per_day)
print(mean_total_per_day)
print(median_per_day)

num = len(mydictionary)
meantotalperday = tuple(mean_total_per_day.values())
groups = np.arange(num)   
width = 0.6     

plotting = plt.bar(groups, meantotalperday, width)
plt.ylabel('Numbers of Steps ')
plt.title('Mean Total Step a Day')
plt.xticks(groups, tuple(mean_total_per_day.keys()))
plt.yticks(np.arange(0, 300, 20))

plt.show()


import csv
import statistics
import numpy as np
import matplotlib.pyplot as plt

with open('activity.csv', 'r') as a:
    data = csv.reader(a)
    mydictionary = {}
    for row in data:
        if row[0] != 'NA' and row[0] != 'steps':
            if row[2] not in mydictionary:
                mydictionary[row[2]] = [int(row[0])]
            else:
                mydictionary[row[2]].append(int(row[0]))

print(mydictionary)

total_pertime = {}
mean_total_pertime = {}
median_pertime = {}
for key, value in mydictionary.items():
    total_pertime[key] = sum(value)
    mean_total_pertime[key] = round(statistics.mean(value),2)

#print(totalpertime)
#print(mean_totalpertime)

#graph
plt.plot(list(mean_total_pertime.keys()), list(mean_total_pertime.values()))
plt.xlabel("Time")
plt.ylabel("Steps each 5 Time")
plt.show()
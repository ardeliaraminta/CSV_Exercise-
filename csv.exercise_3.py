import csv
import statistics
from statistics import mean 
from statistics import median
import numpy as np 
import matplotlib.pyplot as plt 

with open('activity.csv','r') as file:
    datas = file.readlines()
    datas.pop(0)
    maximum_average = {'steps':0,'date1':'','date2':''}
    minute_data = {d:0 for d in [y.split(',')[2].split("\n")[0] for y in datas]}
    current_data = {}
    total_day = len([y for y in [z for z in datas]]) / len(minute_data.items())
    for data in datas:
        if not data.split(',')[0]=='NA':
            minute_data[data.split(',')[2].split('\n')[0]] += int(data.split(',')[0])
            if current_data.get('steps') == None:
                current_data['steps'] = data.split(',')[0]
                current_data['date'] = data.split(',')[1] +':'+ data.split(',')[2].split('\n')[0]
            else:
                if not current_data['steps'] =='NA':
                    step_difference = (int(data.split(',')[0]) - int(current_data['steps']))
                    if step_difference > maximum_average['steps']:
                        maximum_average['steps'] = step_difference
                        maximum_average['date1'] = current_data['date']
                        maximum_average['date2'] = data.split(',')[2].split('\n')[0]
                current_data['steps'] = data.split(',')[0]
                current_data['date'] = data.split(',')[1]+':'+ data.split(',')[2].split('\n')[0]
        else:
            current_data['steps'] = 'NA'
            current_data['date'] = data.split(',')[1] + ':' + data.split(',')[2].split('\n')[0]
    minute_data = {d:(y/total_day) for d,y in minute_data.items()}
    print(maximum_average)
    #print(minute_data)
    input('Please enter to show graph')
    plt.plot([y for y in minute_data.keys()],[z for z in minute_data.values()])
    plt.xlabel('Time Interval')
    plt.ylabel('Average number of steps')
    plt.show()



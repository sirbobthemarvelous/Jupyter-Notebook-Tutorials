import pandas as pd
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt

#print(plt.style.available) to show all available styles built into matplotlib
plt.style.use("ggplot") #is an example of using it, bmp, fast, seaborn

ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_indexes = np.arange(len(ages_x)) #creates an array of numbered version of the x values
width = 0.24    #variable to be the distance between the plotting

py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
plt.bar(x_indexes - width, py_dev_y, width = width, label='Python') 
# you can add lineplots alongside bars or add bars next to it
# add the width value and make it equal to the distance between x values

js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
plt.bar(x_indexes, js_dev_y,width = width, label='JavaScript')

dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
plt.bar(x_indexes + width, dev_y, width = width, color='#444444', label='All Devs')
#you have to make sure number of items in the list are the same for both x and y
#you have to use numpy to put a set indent between the bar graphs

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')

plt.legend() 
plt.xticks(ticks=x_indexes, labels=ages_x) # to keep the age values to be visible rather than the indexes

plt.tight_layout() #makes padding better

plt.show()

#CSV Analysis:
#ways to upload csv: 1. csv module 2. readcsv form pandas 3. loadcsv from numpy
#standard library: import csv and then  "with open('data.csv') as csv_file:"
# csv_reader = csv.DictReader(csv_file)     (it's an iterator that loops too)
# row = next(csv_reader)    Print(row) and then it'll show the headers and first responses
#you might need to mention row['thing'].split('delimiter')

#counter is an imported thing from collections
#you can add things to it like a dictionary
# language = Counter()
# for row in csv_reader:
# language.update(row['languagesThing'].split('delimiter'))
# print language or language.most_common(15) for top 15     jupyter has an easier version
# you can make an x and y axis using this dictionary and a for loop too

#readcsv from pandas
#data = pd.read_csv('data')
#ids = data['column 1'] the x axis
#lang - data['column 2'] the y axis
#use the same Counter update thing
# for response in lang:
#   lang.update(response.split('delimiter'))

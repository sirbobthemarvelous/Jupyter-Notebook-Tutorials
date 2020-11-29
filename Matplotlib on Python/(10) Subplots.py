import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('ggplot') 

data = pd.read_csv('data.csv')

plt.title('List of Ages')
plt.tight_layout() 
plt.show()

#to make a subplot in a csv .plot()

#fig, ax = plt.subplots()
#replace plt.plot with ax.plot()
#ax.legend() 
#plt.set_title(), set_xlabel, set_ylabel etc for the labels
#fig, ax = plt.subplots(nrows=2,ncols=1) you can set rows and columns of plots
#you can do ax1 and ax2 to make individual subplots, 2 separate plots with One Figure of Statistics
#sharex=True, shares the x axis
#you can do fig1,ax1 ...fig2,ax2 for another version to make it two windows



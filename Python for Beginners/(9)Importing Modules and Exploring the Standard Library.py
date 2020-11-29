import sys
#importing modules checks through a list called Sys.path
sys.path.append('/Users/robzh/Documents/python/RobMods')
# or you can add python paths into your computer
from firstModule import find_index, test  #or use * for everything
# or  just say from firstModule import find_index if you just want that instead of the entire module


things = ['Robert', 'ice cream', 'panda', 'Karkat']

index = find_index(things, 'Karkat') #you can shorten find_index with fi
print(index)
print(test)

print(sys.path) #this is the list and we can do list methods on it

#useful modules:
#random: randomThing = random.choice(array or list), print (randomThing)
#math:  rads = math.radians(degrees of some value), math.sin(rads) get sin value via rads
#datetime and calendar: datetine.date.today() = 2020-09-22, calendar.isleap(2020) = true
#os:    os.getcwd() aka current working directory
import os
print(os.getcwd())
print(os.__file__) #prints out location of the os file

#anti gravity just leads to the xkcd comic
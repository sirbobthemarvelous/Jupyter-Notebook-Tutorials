import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight') 

x_vals = []
y_vals = []

plt.plot(x_vals,y_vals)

index = count()

def animate(i): 
  x_vals.append(next(index))
  y_vals.append(random.randint(0,5))
  plt.cla() #clear it out before new plot comes
  plt.plot(x_vals,y_vals) #plotting every secondish

ani = FuncAnimation(plt.gcf(), animate, interval = 1000)
#gcf get current figure

plt.title('Best Pie Chart')
plt.tight_layout() 
plt.show()

# data = pd.read_csv('data.csv')
# x = data['x_value']
# y1 = data['total_1']
# y2 = data['total_2']

#writing data into csv in real time
# import csv
# import random
# import time

# x_value = 0
# total_1 = 1000
# total_2 = 1000

# fieldnames = ["x_value", "total_1", "total_2"]


# with open('data.csv', 'w') as csv_file:
#     csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     csv_writer.writeheader()

# while True:

#     with open('data.csv', 'a') as csv_file:
#         csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

#         info = {  #the labels
#             "x_value": x_value,
#             "total_1": total_1,
#             "total_2": total_2
#         }

#         csv_writer.writerow(info)
#         print(x_value, total_1, total_2) #console info

#         x_value += 1
#         total_1 = total_1 + random.randint(-6, 8) #change every time
#         total_2 = total_2 + random.randint(-5, 6)

#     time.sleep(1)
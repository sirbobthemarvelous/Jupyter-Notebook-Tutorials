import pandas as pd
from matplotlib import pyplot as plt

# data = pd.read_csv('data.csv')
# labels = data['Treatment']
# avgLDH = data['avg released LDH']
# LDHttest = data['LDH ttest']
# MTTttest = data['MTT ttest']

# plt.plot(avgLDH, LDHttest, color='#444444', linestyle='--', label = "onecler") 

# plt.plot(avgLDH, MTTttest, label='Mario')

# #you can add an overall median to add as a third value/argument to only fill above or below a specific line
# #where = (MTTttest>overall_median), only fills when above and ,interpolate=True stops x clipping
# plt.fill_between(avgLDH, MTTttest, alpha=0.25)
#alpha makes the filling a bit more see through

#you can repeat that fill between but only include the below part and change the color
#you can also do conditionals with other plots, label the filling with a legend too


plt.legend()

plt.title('Who knows')
plt.xlabel('released LDH')
plt.ylabel('ttests')
plt.tight_layout() 
plt.show()
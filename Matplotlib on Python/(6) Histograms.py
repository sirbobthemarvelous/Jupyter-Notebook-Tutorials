from matplotlib import pyplot as plt

plt.style.use('seaborn') 

ages = [18,19,21,25,26,26,30,32,38,45,54]
bins = [10,20,30,40,50,60] #5 bins using 6 points

plt.hist(ages, bins=bins, edgecolor='black', log=True) 
#either put an integer and divide them automatically into like 5 groups
#or explicitly put some specific bins
#edgecolor to differentiate them since they have no space in between
#log adds in scientific notation

plt.axvline(29, color='red', label='median') #access verticle line
plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout() 
plt.show()
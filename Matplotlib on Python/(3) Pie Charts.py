from matplotlib import pyplot as plt

plt.style.use('ggplot') 

slices = [65,45, 3, 20]
labels = ['sexy','ye', 'platypus', 'doof']
colors = ['red','green','cyan','magenta'] #you can use hexcodes
explode =[0,0,0,0.1] #list of floats that shows how much we want to emphasize a sice by pushing it from the center

plt.pie(slices, labels=labels, colors=colors ,explode=explode, shadow= True, 
startangle=90, autopct='%1.1f%%', wedgeprops={'edgecolor':'black'}) 
#piechart shows proportion number doesn't have to add up to 100
#wedgeprops adds an outline
#shadow adds a shadow, startAngle sets a specific angle
#autopct shows the percentage using a format string 

plt.title('Best Pie Chart')
plt.tight_layout() 
plt.show()
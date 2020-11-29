from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight') 

minutes = [1,2,3,4,5,6,7,8,9]

player1 = [8,6,5,5,4,2,1,1,0]
player2 = [0,1,2,2,2,3,3,4,4]
player3 = [0,1,1,2,3,3,4,5,5]

labels = ['player1','player2','player3']
colors = ['#ffbb32','#f676e0','#86eb8a']

plt.stackplot(minutes,player1,player2,player3, labels=labels, colors=colors) #x axis and all the y axises stacking on top

plt.legend(loc='lower left') #make the legend appear on a different corner
#you can also use loc=(0.07,0.05) to use a tuple to set the legend

plt.title('Best Stack Plot')
plt.tight_layout() 
plt.show()
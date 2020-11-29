
horses = ['Howard', 'Mark', 'Phillip', 'Connie'] #a list of strings
gorse = ['Carl', 'June']
wumbers = [1,4,2,3,5]

print(horses.append('Ashley')) #appends another value to the end
print(horses.insert(0,'Vriska')) #insert it at a specific index place
#you can also insert a List instead of Just a value
print(horses.extend(gorse)) # appends a List as a Single index
print(horses.remove('Howard')) #removes a thing
popped = horses.pop() #removes the last item on the List, useful for Stacks
print(popped) #it also returns the last item on the List which you removed
gorse.reverse() #reverses the order
horses.sort() #sort by alphabetical order or by a specific number order 
#you can use .sort(reverse=True) to sort it in Reverse order
borted = sorted(horses)  #gives a sorted version without Sorting it
print(borted)
print(min(wumbers)) #return minimum number of list of numbers
# max() returns max number, sum() returns sum of numbers in the list
print(horses.index('Vriska'))   #gives u the index of the thing in the list
print('Mark' in horses) #gives whether it's true something is within the List

for index,thing in enumerate(horses): #loops through a List
    print(index, thing) #enumerate gives the index number next to all of them

print(horses) #prints out the values
#len(list) just gives you the number of indecies not the string length
print(horses[3]) #prints out a specific item in the list
print(horses[-1]) #use negative numbers to go backwards, -1 is the last item
print(horses[0:3]) #its like a substring for lists [)
#or just use horses[:3] and it'll assume it starts from the beginning

horseStr = 'chain'.join(horses) #prints out the things with a phrase joining them together
horseSpl = horseStr.split('chain') #split this string into parts based on the delimiter
print(horseStr)
#lists are mutable, Tuples are NOT
Torses = ('Firefox','Chrome','Tor', 'Safari') #tuples use paranthasis

#Sets use curly brackets
Sorses = {'Bob','Ally', 'Micheal','Sarah'} #Sets don't care about order, used to check Inclusion and Duplicated 
OVAses = {'Zyfre', 'Dylan', 'Sarah', 'Ally'}
print(Sorses)
print('Bob' in Sorses) #check if it's in there
print(Sorses.intersection(OVAses)) #checks similar elements
#.difference(OVAses) would show the ones that aren't shared
#.union(OVAses) would show all elements in both without duplicates

emptyList = []  #or list()
emptyTuple = () #or tuple()
emptySet   = set()  # {} would make an empty DICTIONARY


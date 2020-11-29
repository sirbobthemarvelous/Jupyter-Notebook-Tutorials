
mnessage = 'heyo World'
print(mnessage)
var1able = "Milo 'lucky' Murphy"   #you can use double quotes if you want single quotes in the message
print(var1able)
print (len(var1able)) #prints out the Length of the message rather than the message itself
print(var1able[2]) #prints out the 3rd character of the Array that is a String
print(mnessage[0:4]) #prints out the substring of heyo [)
print(mnessage[5:]) #print from W to the end so u get World
#methods are just functions that belong to an object, otherwise they're the same
print(var1able.lower()) #all lower case, .upper() causes it to be all uppercase
print(var1able.count('m')) #counts all the times a specific phrase appears
#.find('something') returnsthe index that the phrase begins at
mnessage = mnessage.replace('World','Cat') #replaces phrase with another phrase
print(mnessage)
print(var1able + ',' + mnessage + '. Welcome!') #concatenating 

formatted = '{}, {}. WELCOME!'.format(mnessage,var1able) #use brackets to add placeholders/arguments
#recently released: f strings
fformatted = f'{var1able}, {mnessage.upper()}. WELCOME!' #you can directly add the strings into the brackets

#dir function
print(dir(mnessage)) #gives lists of attributes and methods available
print(help(str)) # gives list and explaination of all string methods
#or you could simplify it with
print(help(str.upper)) #only gives info on the upper method

print('Hello World')

numb = 3
floatt = 3.14
print(type(numb)) #returns type of variable
print(type(floatt)) #this'll be a float instead of an integer

#Arithmetic Operators:
# Addition: +       Subtraction: -
#Multiplication: *  Division:   /   Floor Division: //
#Exponent:      **  Modulus:    % (get the remainder of division)

numb *= 10
floatt += 10    #multiply and add by ten respectivly
print(round(4.12)) #rounds a number
print(round(4.12,2)) #round to a specific amount
print(numb == floatt) #checks whether or not it's equal and releases true or false
#or != to check if it Isn't Equal, releases True if it ISN't Equal
# Greater than or equal to : >= , <=, > , < they're all useable too

garlics = '101'
cloves = '823'
#they're strings right now, but you can Cast them as integers
numGarlics = int(garlics) #integer version of garlics
cloves = int(cloves) #do it to itself too
print(numGarlics + cloves)



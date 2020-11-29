
def hewwo_there(): #define function with arguments
    print('sup')
    pass            #doesn't do anything just lets it end

print(hewwo_there) #prints out function information
hewwo_there() #executes function

#keeping your code "dry" means to keep yourself from repeating code 

def greeting():
    return ('salve')
print(greeting().upper()) #string methods work on returned strings

def customGreeting(greet, name='You'): #you can add default values in the arguments
    return '{}, {} Function.'.format(greet, name)
print(customGreeting('heyo'))
print(customGreeting('hewwo',name = 'Asher'))

def stars(*aaa, **blah): #the stars means that it can be any type with random values
    print(aaa)  #tuples in this case
    print(blah) #dictionary in this case
names = ['Greg', 'Estelle']
info = {'gem': 'garnet', 'age':40}

stars('Steven', 'Rose', gem = 'quartz', age =4)
# or
stars(*names, **info)


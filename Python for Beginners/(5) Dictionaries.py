#key value pairs are like Hash Maps
#word is key, definition is value , in the dictionary metaphor

apprentice = {'name':'firepaw', 'age': 0.5, 'courses': ['Boxing', 'Hunting']}
apprentice['phone'] = '143-1025' #appends it since it didn't exist before
apprentice['name'] = 'fireheart'
#or you can do it onmass like
apprentice.update({'name':'Firestar','age':4, 'phone':'16'})
del apprentice['phone']     #removes a value by key
age = apprentice.pop('age')     #removes value but also releases it
print(age)
print(len(apprentice)) #returns length...aka #of keys
print(apprentice.keys()) #return only keys
#.values() returns only values, .items() returns all the duos in pairs

#loops default only go through the keys
for key in apprentice:
        print(key)
for key, value in apprentice.items(): #edited so u can get both
        print(key, value)


print(apprentice['courses'])
#key can be an integer if you want, or just any immutable data type
print(apprentice.get('name')) #get the value, doesn't throw an error like square brackets do

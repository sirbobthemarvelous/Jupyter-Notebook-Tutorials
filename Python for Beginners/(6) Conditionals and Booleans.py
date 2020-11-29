#Comparisons:
# == is for equality , Object Identity: is
# >=, <=, <, > etc. != not equal
lang = 'Python'
if lang == 'Python':
    print('language is python')
elif lang == 'Spanish':
    print('Language is Spanish')
else:
    print('nope')

month = 'march'
if lang == 'Latin' and month == 'march': #and operator, you can also use or as an operator
    print('beware the ides of march')
else:
    print('???')
if not lang == 'Latin':
    print('latin is a dead language')

#if you have two different variable that are equal, == will provide true, but IS will provide false because they're distinct
#they're checking the variable id
print(id(lang))
print(id(month))
#(a is b) is basically (id(a)==id(b))

#values that count as false in conditionals:
#False, None, Zero in numeric type, empty sequence like '',(),[]
#or empty mapping like {} which is an empty dictionary
    #if 0: counts as if False:


magic = [413,612,1025,8,1111]

for god in magic: #goes through and prints it out, cecking for 8
    if god == 8:
        print('Vriska Spotted')
        break
    print(god)
#break keyword breaks the loop
#continue keyword ends the iteration and continues loop

for num in magic: #nested loops, looping through combinations
    for alpha in 'kxd':
        print(num, alpha)

#running the loop a specific number of times
for items in range(3): #0,1,2
    print(items)
for thing in range(1,11): #1 to 10
    print(thing)

#here come while loops
x = 10
while x <17:
    if x == 15:
        break
    print(x)
    x += 1

#you can make infinite loops, use control c to cancel that
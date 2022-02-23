'''
Arnav Bhatia
CIS 41A Fall 2020
Unit G Take Home Assignment
In this assignment, we learn how to read a file, make a dictionary of lists, keys, and sets
'''

#Part One – Reading a data file
states = open('States.txt', 'rt')
lines = states.readlines()
list = []
for line in lines:
    x = line.split()
    regions = x[1:2]
    if regions[0] == 'Midwest':
        list.append(x)
highest_pop = 0
stateAbr = ""
for i in list:
    if int(i[2]) > int(highest_pop):
        highest_pop = int(i[2])
print("Highest population state in the Midwest is: IL", highest_pop)
print()

#Part Two – A Dictionary of Lists
presidents = open('USPresidents.txt', 'rt')
lines = presidents.readlines()
usPresidents = dict()
for line in lines:
    y = line.split()
    if y[0] in usPresidents:
        usPresidents[y[0]].append(y[1])
    else:
        usPresidents[y[0]] = [y[1]]
keyValue = ""
length = 0
for key in usPresidents:
    if len(usPresidents[key]) > length:
        length = len(usPresidents[key])
        keyValue = key
print("The state with the most presidents is", keyValue, "with", length, "presidents:")
for value in usPresidents[keyValue]:
    print(value)
print()

#Part Three – Dictionary Keys and Sets
statePresidents = open('USPresidents.txt', 'rt')
lines = statePresidents.readlines()
presidentsDict = dict()
value = 1
for line in lines:
    z = line.split()
    if z[0] in presidentsDict:
        presidentsDict[z[0]] += 1
    else:
        presidentsDict[z[0]] = value
States = ("CA", "TX", "FL", "NY", "IL", "PA", "OH", "GA", "NC", "MI")
popularStates = set()
for val in States:
    if val in presidentsDict:
        popularStates.add(val)
print(len(popularStates), "of the 10 high population states have had presidents born in them.")
for val in popularStates:
    if val in presidentsDict:
        print(val,presidentsDict[val])

'''
Execution Results:
Highest population state in the Midwest is: IL 12802000

The state with the most presidents is VA with 8 presidents:
George_Washington
James_Madison
James_Monroe
John_Tyler
Thomas_Jefferson
William_Henry_Harrison
Woodrow_Wilson
Zachary_Taylor

8 of the 10 high population states have had presidents born in them.
IL 1
GA 1
OH 7
NC 2
NY 5
CA 1
TX 2
PA 1
'''
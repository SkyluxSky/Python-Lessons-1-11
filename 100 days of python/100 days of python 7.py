# take 2 digits, x and y as inputs and generate a 2 dimensional array
#This program creates rows and columns in an array

input_for_system = input('Type input here: ')
dimension = [int(x) for x in input_for_system.split(',')]
rowin = dimension[0]
colin = dimension[1]
list = [[0 for column in range (colin)] for rows in range(rowin)]

for row in range(rowin):
    for col in range(colin):
        list[row][col] = row*col
print(list)
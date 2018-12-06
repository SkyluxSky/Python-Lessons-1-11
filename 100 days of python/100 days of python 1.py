#find all numbers divisible by 7 but NOT a multiple of 5 between 2000 and 3200
#Solution should be comma seperated on a single line

#empty_list: <class 'list">: []
empty_list = []

#iterate through the range of numbers
#An 'i' can be any number

for i in range(2000,3201):
    if (i%7 == 0) and (i%5 != 0):
        empty_list.append(str(i))

print(','.join(empty_list))

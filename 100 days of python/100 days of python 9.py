# Create an array of 5 intergers and display array items, access viw index
from array import *
array_num = array('i', [1,3,5,7,9])
for i in array_num:
    print(i)
print('Access first three items individuals')
print(array_num[0])
print(array_num[1])
print(array_num[2])

# append a new item at the end of an array

print('starting array', array_num)
array_num.append(11)
print('new array', array_num)

# reverse order of the array
print(array_num[::-1])

# insert a new value before the number 3

print(array_num)
# I want to inser the number 4 at index of 2
array_num.insert(2,4)
print(array_num)

# remove an item via index
array_num.pop(3)
# default is last item, otherwise add index
print(array_num)

# remove the first occurance of an element

new_array = array('i', [1,3,5,7,3,9,3,11])
print('new array: ', new_array)
new_array.remove(3)
print(new_array)

# convert an array into a list

print(type(new_array))
x = new_array.tolist()
print(type(x))


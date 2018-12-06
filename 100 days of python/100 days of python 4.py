#Lists can be messed with you can add delete or move information within them
#Lists are Mutable which means can be mutated

#Tuples cannot be mutated or changed
#Is used in the financial sector when dealing with fixed amounts
#Tuples can be used in PEN testing


values = input("Give me some comma separated numbers:")
list = values.split(',')
tuple = tuple(list)
print(list, tuple)
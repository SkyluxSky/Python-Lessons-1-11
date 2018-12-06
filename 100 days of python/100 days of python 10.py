# revers an input str

x = input('Type what do you want to reverse.... ')
b = ''.join(reversed(x))
print(b)

# or, use a start end step. slices str steps of -1

print(x[::-1])

# count even or odd from a series of numbers
# \t is tab over

def oddEvenCount(x):
    odd_count = 0
    even_count = 0
    for i in x:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return "odd count: " + str(odd_count) + "\teven_count: " + str(even_count)

x = [1,2,3,4,5,6,7,8,9,10,11]
print(oddEvenCount(x))

# given the below list, print out the items and its type

data = [1452, 11.23, 1*2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for icecream in data:
    print('Type of ', icecream, ' is ', type(icecream))

# write a program prints all numbers except 3 and 6

for i in range(7):
    if i != 3 and i != 6:
        print(i)
print('\n')

# program a fibonacci sequence between 0 and 50. next number is found by adding 2 numbers before it

x,y = 0,1
while y < 50:
    print(y)
    x,y = y, x+y

print('\n')

# write a program iterating 0 to 50. If num is multiple of 3 print SUPAA instead of num.
# if num is multiple of 5 print BADASS. If num is multiple of both print SUPAA BADASS.

for fizzbuzz in range(1,50):
    if fizzbuzz % 3 == 0:
        print("SUPAA")
    elif fizzbuzz % 5 == 0:
        print("BADASS")
    elif fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("SUPAA BADASS")
    else:
        print(fizzbuzz)
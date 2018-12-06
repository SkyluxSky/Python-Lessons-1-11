#Create a cool calculator
c = 50
h = 30
#use this formula Q = square root of [(2*c*d)/h]
#find d

import math
x = []
y = [i for i in input('give me a number: ').split(',')]
for d in y:
    x.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print(','.join(x))

#The join method is for str so we need to convert our interger answer to a str to
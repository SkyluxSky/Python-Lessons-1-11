#given intergral number n, create a dictionary with the function that creates the key value
#Intergral is a number assigned to a function
#dict() starts an empty dictionary

print('enter in a number:')
n = int(input())
d = dict()
for i in range(1, n+1):
    d[i] = i*i
print(d)
# recall that the range will go up to and not include
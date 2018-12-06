pets = ['dog', 'cat', 'bird', 'rabbit', 'fish', 'neighbor']

# To get each item in list printed I could....

print(pets[0])
print(pets[1])
print(pets[2])
print(pets[3])
print(pets[4])
print(pets[5], '\n')

# or use a for loop

for animals in pets:
    print(animals)
# ^^^^^ This is how you write a program to write out a list without writing Print1 Print 2 Print3 etc....


# rock out a conditional statement with a while loop

i_got_20_bucks = 20

while i_got_20_bucks < 35:
    print(i_got_20_bucks)
    i_got_20_bucks += 1
print('I need more money')

# never forget the infinite code = meaning it never hits a false
# ^^^^^^^^^^^^^^^^^^^^^
# x = 5
# while x > 3: #make this conditional true for an infinite loop
#     print('This was very dumb to run')

# For all numbers between 1500 and 2700, which are divisible by 7 and multiple of 5

for i in range(1500,2700):
    if i%7==0 and i%5==0:
        print(i)

# write a program that will guess a number between 1 and 10

import random
target_num, guess_num = random.randint(1,10), 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10, and keep guessing until you are correct'))
print('Game Over')

# Create a cool printed pattern that looks like a sideways triangle

count = 0
for num in range(7):
    count += 1
    print('*' * count)
for num in range(6):
    count -= 1
    print('*' * count)

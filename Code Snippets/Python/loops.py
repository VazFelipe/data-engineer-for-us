# Python Loops

# source https://realpython.com/python-while-loop/

# while loop
# indefinite iteration: the number of times the loop is executed 
# isn’t specified explicitly in advance. Rather, the designated block 
# is executed repeatedly as long as some condition is met.

i = 0

while i < 3:
    print('do something')
    i += 1

# source https://realpython.com/python-for-loop/

# for loop
# definite iteration, the number of times the designated block will be executed
# is specified explicitly at the time the loop starts.
# as i is not called in the for loop we could improve the code by tiping _ 
# for i in range(3):
for _ in range(3):
    print('do something')

# pythonic way of for loop
# but less readable
print('do something\n' * 3, end='')

# asking the user for some particular return n times
while True:
    n = int(input("What´s n? "))
    if n < 0:
        # using the keyword continue to keep on that loop until 
        # the user returns what I've asked
        continue
    else:
        # if n is greater or equal to 0 then stop asking the user
        # we are ready to go, so break
        break

# too much code, let's reduce this complexity
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print('do something')

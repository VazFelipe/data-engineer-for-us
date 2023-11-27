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
    n = int(input("What's n? "))
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

# for loop from lists
# Just remeber: Python lists can hold arbitrary elements
# everything is an object in Python, including functions
# loop into the list will require us to now how many elements are there
# we will use range and len methods to help us
# more details in https://docs.python.org/3/tutorial/datastructures.html#tut-loopidioms

things = ['me', 'you', 'us', 33]

for thing in range(len(things)):
    print(things[i])

# reprompt the user to input values again
# source: https://stackoverflow.com/questions/55437419/how-to-use-the-try-except-command-in-a-while-loop-asking-for-user-input

while True:
    try:
        my_integer = int(input("Please give an integer number"))
    except ValueError:
        print("This was not a valid input please try again")
    else:
        break  # <-- if the user inputs a valid score, this will break the input loop

print ("my integer is:", my_integer)

# teste fim
plantas = ["tomate","banana","maça","melancia","abacate","laranja"]
contador = 0
max_plantas = len(plantas)

while True:
    mensagem = f'Rega a planta {plantas[contador]}'
    print(mensagem)
    contador += 1

    if contador == max_plantas:
        break

# teste início
while contador < max_plantas:
    mensagem = f'Rega a planta {plantas[contador]}'
    print(mensagem)
    contador += 1
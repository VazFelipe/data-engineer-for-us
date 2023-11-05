# From CS50 Introduction to Programming with Python
# I rewrote some lines to be more generic
# I have not controlled exceptions
# For generic explanations about loops go to the main index and look for loops.py

def main():
    """Prints Do something n times.
    """
    number = get_number_times()
    do_something(number)

def get_number_times():
    """Naive ask user how many times reproduce Do something.
    """
    n = int(input("How many times would you like? "))
    while True:
        if n > 0:
            break
    return n

def do_something(n):
    """Reproduce Do something n times.

    Args:
        n (integer): the number of times Do something will be reproduced.
    """
    for _ in range(n):
        print("do domething")

main()
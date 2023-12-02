# def main():
#     """Prints Do something n times.
#     """
#     number = get_number_times()
#     do_something(number)

# def get_number_times():
#     """Naive ask user how many times reproduce Do something.
#     """
#     n = int(input("How many times would you like? "))
#     while True:
#         if n > 0:
#             break
#     return n

# def do_something(n):
#     """Reproduce Do something n times.

#     Args:
#         n (integer): the number of times Do something will be reproduced.
#     """
#     for _ in range(n):
#         print("do domething")

# main()


# my_list = ['um', 'dois', 'tres']

# for i in range(len(my_list)):
#     print(my_list[i])


# coin = [25, 10, 5]

# enter = int(input())

# if enter in coin:
#     print("valeu")
# else:
#     print("n valeu")


# vanity_plate = 'CS05'
# reversed = vanity_plate[::-1]
# count = ''

# # print(reversed[0])

# if reversed[0].isalpha():
#     print(None, 'aqui')

# for letter in vanity_plate:
#     if letter == '0':
#         print(None, 'aqui2')
#     else:
#         vanity_plate

plate = '0A'

if plate.isnumeric():
    print(True)

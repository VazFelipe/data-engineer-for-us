# using conditionals
# def main():
#     if evaluate_options():
#         print('yes')
#     else:
#         print('no')

# def evaluate_options():
#     answer = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ').lower().strip()
#     options_list = ['42', 'forty-two', 'forty two']
#     return answer in options_list

# main()

# using filter
# def deep_thought():
#     great_question = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ').lower().strip()
#     answer = ['42', 'forty-two', 'forty two']
#     result = list(filter(lambda option: option in great_question, answer))
#     if result:
#         print('yes')
#     else:
#         print('no')

# using map
# def deep_thought():
#     great_question = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ').lower().strip()
#     answer = ['42', 'forty-two', 'forty two']
#     result = any(map(lambda option: option in great_question, answer))
#     if result:
#         print('yes')
#     else:
#         print('no')

# using reduce
def deep_thought():
    from functools import reduce
    great_question = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ').lower().strip()
    answer = ['42', 'forty-two', 'forty two']
    result = reduce(lambda option_1, option_2: option_1 or option_2 in great_question, answer, False)
    if result:
        print('yes')
    else:
        print('no')

deep_thought()
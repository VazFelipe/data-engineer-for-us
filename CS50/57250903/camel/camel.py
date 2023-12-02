def main():
    """ From a camelCase string return a snake_case.
    """
    camel_to_snake_case()

def camel_to_snake_case():
    """ User's input a camelCase string and it converts to snake_case

    #Parameters:result
    #    user_input(str):The string in camelCase.

    #Returns:
    #    snake_case(str):The string in snake_case.
    """
    # empty string that receives transformation
    snake_case = ""

    # user input a camelCase string
    user_input = input("camelCase: ")

    # for every letter in the camelCase string
    for letter in user_input:

        # if the letter is capitalized
        if letter.isupper():

            # concatenate with underscore and lower it
            letter = "_" + letter.lower()

        # out of if statment the empty string will
        # receive true and false cases
        snake_case += letter

    print(f"snake_case: {snake_case}")

main()

def main():
    """Remove all vowels from user input and print only the consonants
    """
    remove_vowels()


def remove_vowels():
    """Verify each letter of the user input and remove the vowels

    Parameters
    user_input(str): asks user for a string
    vowels(list): list all vowels in all cases

    Return
    result(str): user input with only consonants
    """
    user_input = input("Input: ")
    vowels = ["A", "E", "I", "O", "U",
              "a", "e", "i", "o", "u"]

    result = ""

    for letter in user_input:
        if letter not in vowels:
            result += letter

    print(result)


main()

def main():
    """Remove all vowels from user input and print only the consonants
    """
    word = input("Input: ")
    shorten(word)


def shorten(word):
    """Verify each letter of the user input and remove the vowels

    Parameters
    word(str): asks user for a string
    vowels(list): list all vowels in all cases

    Return
    result(str): user input with only consonants
    """
    vowels = ["A", "E", "I", "O", "U",
              "a", "e", "i", "o", "u"]

    result = ""

    for letter in word:
        if letter not in vowels:
            result += letter

    return result


if __name__ == "__main__":
    main()

# python install inflect

import inflect

def main():
    prompt_user()

def prompt_user():
    """
    Prompt the user to enter names and print a farewell message.

    This function continuously prompts the user to enter names until an EOFError is raised.
    After that, it joins the entered names using the inflect library and prints a farewell message.

    Args:
        None

    Returns:
        None
    """
    p = inflect.engine()

    user_list = []
    try:
        while True:
            user_input = input("Name: ")
            user_list.append(user_input)
    except EOFError:
        message = f'Adieu, adieu, to {p.join(user_list)}'
        print(message)

main()

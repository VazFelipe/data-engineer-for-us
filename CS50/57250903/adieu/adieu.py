import inflect

def main():
    prompt_user()

def prompt_user():
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

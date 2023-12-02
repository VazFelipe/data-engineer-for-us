import emoji

def main():
    convert_message()

def convert_message():
    user_input = input("Input: ")
    output = emoji.emojize(user_input, language='alias')
    return print(f'Output: {output}')

main()

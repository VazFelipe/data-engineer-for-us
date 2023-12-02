import sys
from pyfiglet import Figlet

def main():
    print(program())


def program():
    arguments = args_entering()

    user_input = input("Input: ")

    try:
        if arguments == 'random':
            input_conversion = f.renderText(user_input)
            return f'Output: \n{input_conversion}'
        else:
            f = Figlet(font=sys.argv[2])
            input_conversion = f.renderText(user_input)
            return f'Output: \n{input_conversion}'
    except:
        sys.exit('Invalid usage')
    finally:
        sys.exit


def args_entering():
    f = Figlet()
    fonts = f.getFonts()

    args_size = len(sys.argv)
    if args_size == 1:
        return 'random'
    elif args_size == 3 and ( sys.argv[1] == '-f' or sys.argv[1] == '--font' ):
        if sys.argv[2] not in fonts:
            return sys.exit('Invalid usage')
        return 'specific'
    else:
        return sys.exit('Invalid usage')


main()

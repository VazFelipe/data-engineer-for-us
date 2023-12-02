# Requirements
## The program will prompt the user for a basic arithmetic expression (+, -, *, and /)
## We will calculate the and output the results as a floating-point value

def main():
    x, y, z = assign_variables()
    return print(calculate_output(x, y, z))

def prompt_user():
    return input('Expression: ')

def assign_variables():
    try:
        x, y, z = prompt_user().split(' ')
    except ValueError:
        print('Write an arithmetic expression formatted as x y z, with one space between x and y and one space between y and z. Example: 1 + 1')
        x, y, z = prompt_user().split(' ')

    try:
        x = int(x)
        z = int(z)
    except ValueError:
        print(prompt_user())

    return x, y, z

def calculate_output(x, y, z):
    if '-' in y:
        return float('{:.1f}'.format(x - z))
    if '+' in y:
        return float('{:.1f}'.format(x + z))
    if '*' in y:
        return float('{:.1f}'.format(x * z))
    if '/' in y:
        try:
            return float('{:.1f}'.format(x / z))
        except ZeroDivisionError:
            return 0.0

main()
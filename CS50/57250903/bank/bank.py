# Requirements
## If the greeting starts with "hello", then zero
## If the greeting starts with an "h", then 20
## Otherwise 100

def main(assigned_value):
    return print(assigned_value)

def greeting_from_user():
    return input('Greeting: ')

def assign_value():
    greeting = greeting_from_user().lower().strip()
    if "hello" in greeting:
        return '$0'
    if greeting.startswith("h"):
        return '$20'
    else:
        return '$100'

main(assign_value())
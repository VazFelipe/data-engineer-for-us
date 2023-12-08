# Requirements
## If the greeting starts with "hello", then zero
## If the greeting starts with an "h", then 20
## Otherwise 100

def main():
    greeting = input('Greeting: ').lower().strip()
    print(value(greeting))

def value(greeting):
    if "hello" in greeting:
        return 0
    if greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == '__main__':
    main()

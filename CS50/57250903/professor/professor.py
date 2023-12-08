import random


def main():
    level = get_level()
    generate_integer(level)

def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if 0 < level < 4:
                return level
            else:
                raise ValueError
        except ValueError:
            pass

def generate_integer(level):

    try:
        score = 0
        counter = 0
        while counter < 10:

            if level == 1:
                x = random.randint(0,9)
                y = random.randint(0,9)
                sum = x + y
                message = f'{x} + {y} = '
                answer = int(input(message))
                message_retry = f'{x} + {y} = {sum}'

                counter += 1
                if answer == sum:
                    score += 1
                elif answer != sum:
                    print("EEE")

                    counter_retry = 0
                    while counter_retry < 2:
                        answer = int(input(message))
                        counter_retry += 1
                        try:
                            if answer == sum:
                                score += 0
                                break
                            elif counter_retry == 1:
                                print("EEE")
                            elif counter_retry == 2:
                                raise ValueError
                        except ValueError:
                            print("EEE")
                            print(message_retry)

            if level == 2:
                x = random.randint(10,99)
                y = random.randint(10,99)
                sum = x + y
                message = f'{x} + {y} = '
                answer = int(input(message))
                message_retry = f'{x} + {y} = {sum}'

                counter += 1
                if answer == sum:
                    score += 1
                elif answer != sum:
                    print("EEE")

                    counter_retry = 0
                    while counter_retry < 2:
                        answer = int(input(message))
                        counter_retry += 1
                        try:
                            if answer == sum:
                                score += 0
                                break
                            elif counter_retry == 1:
                                print("EEE")
                            elif counter_retry == 2:
                                raise ValueError
                        except ValueError:
                            print("EEE")
                            print(message_retry)

            if level == 3:
                x = random.randint(100,999)
                y = random.randint(100,999)
                sum = x + y
                message = f'{x} + {y} = '
                answer = int(input(message))
                message_retry = f'{x} + {y} = {sum}'

                counter += 1
                if answer == sum:
                    score += 1
                elif answer != sum:
                    print("EEE")

                    counter_retry = 0
                    while counter_retry < 2:
                        answer = int(input(message))
                        counter_retry += 1
                        try:
                            if answer == sum:
                                score += 0
                                break
                            elif counter_retry == 1:
                                print("EEE")
                            elif counter_retry == 2:
                                raise ValueError
                        except ValueError:
                            print("EEE")
                            print(message_retry)

    except ValueError:
        counter += 1

    print(f'Score: {score}')

if __name__ == "__main__":
    main()

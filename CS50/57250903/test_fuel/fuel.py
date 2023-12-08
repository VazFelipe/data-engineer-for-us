def main():
    fraction = "1/0"
    percentage = convert(fraction)
    result = gauge(percentage)

    print(result)

def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError
    elif x > y:
        raise ValueError
    else:
        percentage = round(x / y, 2)
        return percentage

def gauge(percentage):
    if 0.99 <= percentage <= 1:
        message = "F"
        return message
    elif percentage <= 0.01:
        message = "E"
        return message
    else:
        message = "{:.0%}".format(percentage)
        return message

main()

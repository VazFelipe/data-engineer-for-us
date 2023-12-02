def main():
    """
    Returns percentage from a fraction.
    """
    convert_fr_to_per()

def convert_fr_to_per():
    """
    Converts a fraction to percentage.
    Repeats if the input is not a fraction.

    Parameters
    ----------
        user_input (str): any.
        x (int): The dividend.
        y (int): The divisor.

    Returns
    -------
        calculation(int): The quotient of the division (x divided by y).

    """
    while True:
        user_input = input("Fraction: ")

        try:
            x, y = user_input.split("/")

            calculation = int(x) / int(y)

            if calculation > 1:
                raise ValueError
            if 0.99 <= calculation <= 1:
                print("F")
                break
            if calculation <= 0.01:
                print("E")
                break
            else:
                print("{:.0%}".format(calculation))
                break

        except ValueError:
            input("Fraction: ")
        except ZeroDivisionError:
            input("Fraction: ")

main()
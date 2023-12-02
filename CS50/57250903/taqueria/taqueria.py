def main():
    """
    Returns the sum of ordered items in the menu.
    """
    calculate_order()

menu = {
    "Baja Taco": 4.25, "Burrito": 7.50,
    "Bowl": 8.50, "Nachos": 11.00,
    "Quesadilla": 8.50, "Super Burrito": 8.50,
    "Super Quesadilla": 9.50, "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def calculate_order():
    """
    Calculates the cumulative sum of each ordered items in the menu.
    Ctrl + d finish the order.

    Parameters
    ----------
    sum (float): cumulative sum
    order (str): order by user

    Return
    ------
    Cumulative sum formatted as menu currency.
    """
    sum = 0
    try:
        while True:
            order = input("Item: ")
            for key, item in menu.items():
                if order.lower() == key.lower():
                    sum += item
            print(f"Total: ${sum:.2f}")
    except EOFError:
        print("")

main()

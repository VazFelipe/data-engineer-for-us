def main():
    """
    Receive from user the items as a list.
    Returns the count by item in uppercase letter.
    """
    list_count_items()


def list_count_items():
    """
    Get the list os items from user input.
    Count the items in the list and display the count by item in uppercase letter.
    Time complexity O(n^2), due to the usage of count within the for loop.

    Parameters
    ----------
    user_input (str): item from user.
    items (list): full list os items from user.
    items_set (list): list of items with no duplicates.
    count (int): count of items from items.
    join_item (str): items to join with count.

    Return
    ------
    List of items from user and count by items.

    """
    items = []
    try:
        while 1:
            user_item = input()
            items.append(user_item)
            items.sort()
    except EOFError:
        items_set = list(set(items))
        items_set.sort()
        for item in items_set:
            count = items.count(item)
            join_item = "".join(item)

            print(count, join_item.upper())

main()

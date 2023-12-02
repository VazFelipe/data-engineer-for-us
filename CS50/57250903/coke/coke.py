# pseudocode
# start_machine: price definition and
# start_machine: informs the amount due and asks to enter the currency
# cash_in: evaluate the coin typo, the cash_flow and returns the amount due
# amount_due: calculates the amount due


def main():
    machine_price = 50
    accepted_coin = [25, 10, 5]
    start_machine(price=machine_price)
    cash_flow(accepted_coin=accepted_coin, price=machine_price)

def start_machine(price):
    start = f"Amount Due: {price}"
    return print(start)

def cash_flow(accepted_coin, price):
    accepted_coin = accepted_coin
    cash_in = 0

    while cash_in < price:
        coin = int(input("Insert Coin: "))

        if coin not in accepted_coin:
            start_machine(price)
            continue

        cash_in += coin

        if (price - cash_in) == 0:
            print(f"Change Owed: {price - cash_in}")
        if (price - cash_in) < 0:
            print(f"Change Owed: {abs(price - cash_in)}")
        else:
            print(f"Amount Due: {price - cash_in}")

main()

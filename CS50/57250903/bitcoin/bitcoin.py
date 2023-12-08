import sys
import requests
import json

def main():
    request_price()

def evaluate_args():
    args_size = len(sys.argv)
    if args_size == 1:
        evaluation = False
        sys.exit("Missing command-line argument")
    else:
        try:
            args_converted = float(sys.argv[1])
            evaluation = True
        except ValueError:
            evaluation = False
            sys.exit("Command-line argument is not a number")

    return evaluation

def request_price():
    if evaluate_args():
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        output = response.json()

        bitcoin_price = float((output["bpi"]["USD"]["rate_float"]) * float(sys.argv[1]))

        print(f'${bitcoin_price:,}')
    else:
        pass

main()

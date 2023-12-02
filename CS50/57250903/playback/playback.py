def main():
    # Run the funciton to achieve the main objective
    get_input_from_user = replace_input_from_user()
    # Print teh results
    print(get_input_from_user)

def fetch_input_from_user():
    # Ask user anything about him
    fetch_input_from_user = input("Please, could you tell something about you? ")
    return fetch_input_from_user

def replace_input_from_user():
    # Replace every whitespace with three dots
    input_from_user_replaced = fetch_input_from_user().replace(" ", "...")
    return input_from_user_replaced

# Execute the program
main()
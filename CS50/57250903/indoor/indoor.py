def main():
    # Run the funciton to achieve the main objective
    get_indoor_voice_lower = lower_indoor_voice()
    # Print the results
    print(get_indoor_voice_lower)

def fetch_indoor_voice():
    # Ask user to input a string
    fetch = input("Please, tell me what´s in your mind? ")
    # Return the string for consumption
    return fetch

def lower_indoor_voice():
    # Transform the indoor_voice to lower
    indoor_voice_lower = fetch_indoor_voice().lower()
    # Return the string for consumption
    return indoor_voice_lower

# Execute the program
main()
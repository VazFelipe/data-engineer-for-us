# Define emoji patterns
## Define the emoji symbol as Unicode
unicode_smile = "\U0001F642"
unicode_frowning = "\U0001F641"

## Define the emoji symbol as text
text_smile = ":)"
text_frowning = ":("

# Define the main
def main():
    convert_emoji()

# Define the user request
def ask_user():
    # Ask user to input a string
    string_input = input("Could you provide me something in your thoughts? ")
    return string_input

# Define the conversion
def convert_emoji():
    # Replace emoji as text to Unicode
    string_input_replace_smile = ask_user().replace(text_smile,unicode_smile).replace(text_frowning,unicode_frowning)
    # Print results
    print(string_input_replace_smile)

# Execute the main program
main()
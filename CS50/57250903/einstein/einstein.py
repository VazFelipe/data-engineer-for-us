def main():
    einstein_theory = calculate_mass_energy_equivalence()
    print(einstein_theory)

# Pseudocode
def user_input():
    ## The program prompts the user to deliver me the mass as an integer
    input_mass = input("Could you provide me the mass value as integer? ")
    ## I will convert the string to an integer an assign to a mass variable
    mass = int(input_mass)
    return mass

def calculate_mass_energy_equivalence():
    ## Then the program will calculate the Mass-energy equivalency
    speed_of_light = int(300000000)
    mass = user_input()
    energy = mass*pow(speed_of_light,2)
    ## It will be returned to the user as the energy value in Joules
    return energy

# Execute the main program
main()
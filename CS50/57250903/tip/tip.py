def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollar_replace = d.replace("$", "")
    dollars_to_float = round(float(dollar_replace), 1)
    return dollars_to_float


def percent_to_float(p):
    percent_replace = p.replace("%", "")
    percent_to_float = round(float(percent_replace), 2) / 100
    return percent_to_float

main()
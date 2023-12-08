def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if rule_number_1(s) \
        and rule_number_2(s) \
            and rule_number_3(s) \
                and rule_number_4(s) \
                    and rule_number_5(s):
        return True
    else:
        return False


def rule_number_1(vanity_plate):
    count = ""
    for letter in vanity_plate[:2]:
        if not letter.isnumeric():
            count += letter
        count_numeric = len(count)

    if count_numeric in range(1,3):
        return True
    else:
        return False

def rule_number_2(vanity_plate):
    count = len(vanity_plate)

    if vanity_plate.isnumeric():
        return False
    if count in range(2, 7):
        return True
    else:
        return False


def rule_number_3(vanity_plate):
    last_char = vanity_plate[-1]

    len_plate = len(vanity_plate)

    count = 0

    for letter in vanity_plate:
        count += 1
        if letter == '0' and count < len_plate:
            rule_3_1 = False
            break
        else:
            rule_3_1 = True

    if rule_3_1 and not last_char.isalpha():
        return True
    if vanity_plate.isalpha():
        return True


def rule_number_4(vanity_plate):
    for letter in vanity_plate:
        if not letter == '0':
            return True
    return False


def rule_number_5(vanity_plate):
    import string

    for letter in vanity_plate:
        if letter in string.punctuation or letter == ' ':
            return False
    return True


if __name__ == '__main__':
    main()

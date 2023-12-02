def main():
    print(convert_input_iso_8601())

month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def convert_input_iso_8601():
    from datetime import datetime
    user_input = input("Date: ")
    user_input = user_input.strip()
    substring = ","

    try:

        month, day, year = user_input.split(" ")

        if substring not in day:
            convert_input_iso_8601()

        day = day.replace(",", "")

        if day.isalpha():
            convert_input_iso_8601()

        if int(day) > 31:
            convert_input_iso_8601()

        if month.strip() in month_names:
            concat_date = year.strip() + "-" + month + "-" + day.replace(",","").strip()
            date_iso_pre = datetime.strptime(concat_date, "%Y-%B-%d")
            date_iso = datetime.strftime(date_iso_pre, "%Y-%m-%d")
            return date_iso

        if not month.strip() in month_names:
            convert_input_iso_8601()


    except:
        month, day, year = user_input.split("/")

        if month.strip() in month_names:
            convert_input_iso_8601()

        if int(month) > 12:
            convert_input_iso_8601()

        if int(day) > 31:
            convert_input_iso_8601()
        concat_date = year + "-" + month + "-" + day
        date_iso_pre = datetime.strptime(concat_date, "%Y-%m-%d")
        date_iso = datetime.strftime(date_iso_pre, "%Y-%m-%d")
        return date_iso

main()

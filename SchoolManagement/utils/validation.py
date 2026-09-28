def validate_name(name):
    # letters and spaces only, so "Ravi Kumar" is valid
    return name.replace(" ", "").isalpha()


def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10


def get_number(message):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            value = float(input(message))
            if value < 0:
                print("Number cannot be negative.")
            else:
                if value == int(value):
                    value = int(value)      # 85.0 -> 85
                return value
        except ValueError:
            print("Please enter a number.")

# A program that tells the user how many days are in a chosen month

# Dictionary mapping each month number to the number of days
# February is set to 28 by default — will deal with leap years later
days_in_month = {
    1: 31,   # January
    2: 28,   # February
    3: 31,   # March
    4: 30,   # April
    5: 31,   # May
    6: 30,   # June
    7: 31,   # July
    8: 31,   # August
    9: 30,   # September
    10: 31,  # October
    11: 30,  # November
    12: 31,  # December
}

# Ask the user for a month number
# We use try/except in case they type letters instead of a number
try:
    month = int(input("Enter a month number (1-12): "))
except ValueError:
    # If the input wasn't a whole number, show a message and stop the program
    print("That's not a valid number. Please enter a whole number from 1 to 12.")
else:
    # Check that the number is actually a real month
    if month in days_in_month:
        # Special case: February might have 29 days in a leap year
        if month == 2:
            # Ask the user whether it's a leap year (yes/no)
            leap = input("Is it a leap year? (yes/no): ").lower().strip()
            if leap == "yes":
                # In a leap year February has 29 days
                print("February has 29 days in a leap year.")
            else:
                # Otherwise February has 28 days
                print("February has 28 days.")
        else:
            # For all other months, just look up the value in the dictionary
            print("That month has", days_in_month[month], "days.")
    else:
        # If the number isn't between 1 and 12 it's not a valid month
        print("That's not a valid month number. Please pick a number from 1 to 12.")

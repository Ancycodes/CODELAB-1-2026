# This function takes in a number and returns a message
def check_even_or_odd(number):
    # The % operator gives the remainder after dividing
    # If a number divided by 2 has no remainder, it's even
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."


def main():
    # Asks the user for a number and convert it from text to an integer
    user_number = int(input("Enter a whole number: "))

    # Pass the number to the function and store the message it returns
    message = check_even_or_odd(user_number)

    # Print the message from inside main()
    print(message)


# Standard way of starting the program
if __name__ == "__main__":
    main()

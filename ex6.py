# The correct password the user has to guess
correct_password = "12345"

# We give the user a maximum of 5 tries
max_attempts = 5
attempts = 0

# Keep looping until the user runs out of attempts or gets it right
while attempts < max_attempts:
    # Ask the user to type in the password
    guess = input("Enter the password: ")

    # Check if the guess matches the real password
    if guess == correct_password:
        print("Access granted! Welcome.")
        break  # Stop the loop because they got it right
    else:
        # Count this failed attempt
        attempts += 1
        # Work out how many tries are left
        remaining = max_attempts - attempts

        if remaining > 0:
            print(f"Wrong password. You have {remaining} attempts left.")
        else:
            # No tries left — pretend we've alerted the authorities
            print("Maximum attempts reached. The authorities have been alerted!")

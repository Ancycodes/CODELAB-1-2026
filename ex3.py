# Ask the user to type in their details
name = input("What is your name? ")
hometown = input("What is your hometown? ")

# For age I wrap input() in int() so the text gets turned into a whole number
# I use try/except so the program doesn't crash if the user types letters like "twenty"
try:
    age = int(input("What is your age? "))
except ValueError:
    # If the user didn't type a number, show a friendly message and stop
    print("Oops! Age must be a whole number (like 15), not words.")
    exit()

# Store all the information as key-value pairs in a dictionary
# A dictionary is handy because each piece of info has a clear label (key)
biography = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# Prints all three values on separate lines using ONE print() statement
# \n is a special code that means "go to a new line"
print(biography["name"] + "\n" + biography["hometown"] + "\n" + str(biography["age"]))

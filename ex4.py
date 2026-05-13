# Ask the user the question
answer = input("What is the capital of France? ")

# Compare in lowercase so capitalisation doesn't matter
if answer.lower().strip() == "paris":
    print("Correct!")
else:
    print("Wrong!")

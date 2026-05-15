# A list of names to search through
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# The name we are looking for
target = "Sam"

# The simplest way Python's "in" key checks if an item is in a list
if target in names:
    print(f"{target} was found in the list!")
else:
    print(f"{target} is not in the list.")


# Slightly more advanced  use a for loop to find WHERE it is
found = False  # A flag that starts off False
for index, name in enumerate(names):
    # enumerate() gives us both the position (index) and the value (name)
    if name == target:
        print(f"Found {target} at position {index}.")
        found = True
        break  # Stop searching once we've found it (Claude.ai)

if not found:
    print(f"{target} was not found.")

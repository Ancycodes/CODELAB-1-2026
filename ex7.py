# Python's range(start, stop, step) — stop is NOT included, so we go one past

# 1) Count up from 0 to 50 in steps of 1
print("Counting up 0 to 50:")
for i in range(0, 51, 1):
    print(i)

# 2) Count down from 50 to 0 in steps of 1
# Negative step makes the loop go backwards
print("Counting down 50 to 0:")
for i in range(50, -1, -1):
    print(i)

# 3) Count up from 30 to 50 in steps of 1
print("Counting up 30 to 50:")
for i in range(30, 51, 1):
    print(i)

# 4) Count down from 50 to 10 in steps of 2
print("Counting down 50 to 10 in 2s:")
for i in range(50, 9, -2):
    print(i)

# 5) Count up from 100 to 200 in steps of 5
print("Counting up 100 to 200 in 5s:")
for i in range(100, 201, 5):
    print(i)

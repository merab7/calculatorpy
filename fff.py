second = int(input("what's the next number?:   "))
try:
    second = int(second)
except ValueError:
    print("Please enter a valid integer value.")

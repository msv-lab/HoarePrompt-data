s = input()

# Validate input format
if len(s) != 7 or s[0] != "A":
    print("Invalid input")
else:
    # Extract the first two characters after "A"
    digits = s[1:3]

    # Convert the digits to an integer
    number = int(digits)

    # Output the result
    print(number)
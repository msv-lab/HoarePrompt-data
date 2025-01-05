def balanced_shuffle(s):
    n = len(s)
    balance = 0
    data = []

    # Calculate prefix balances and store them with positions
    for i, char in enumerate(s):
        if char == '(':
            balance += 1
        else:
            balance -= 1
        data.append((balance, -i, char))  # Use -i to sort positions in descending order

    # Sort based on balance and position
    data.sort()

    # Build the shuffled sequence
    result = ''.join(char for _, _, char in data)
    return result

# Input handling
s = input().strip()

# Compute and print the balanced shuffle
print(balanced_shuffle(s))

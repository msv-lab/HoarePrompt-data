# Read the input values
n, a, b, c = map(int, input().split())

# Calculate the remainder when n is divided by 4
remainder = n % 4

# If the remainder is 0, Alyona already has the required number of copybooks
if remainder == 0:
    print(0)
else:
    # Calculate the cost to make the total copybooks divisible by 4
    if remainder == 1:
        # We need to add 3 copybooks
        cost = min(3 * a, a + b, c)
    elif remainder == 2:
        # We need to add 2 copybooks
        cost = min(2 * a, b, 2 * c)
    elif remainder == 3:
        # We need to add 1 copybook
        cost = min(a, b + c, 3 * c)
    
    # Print the minimum cost
    print(cost)

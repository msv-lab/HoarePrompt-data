n, p = map(int, input().split())

# Create a set to store the bad pairs of ingredients
bad_pairs = set()

# Read the bad pairs of ingredients and add them to the set
for _ in range(p):
    a, b = map(int, input().split())
    bad_pairs.add((a, b))
    bad_pairs.add((b, a))

# Correctly initialize the list of number of ingredients that can be used in each drink
num_ingredients = [1] + [0] * n

# Calculate the number of ingredients that can be used in each drink
for i in range(1, n + 1):
    num_ingredients[i] = num_ingredients[i - 1] + (i, i + 1 not in bad_pairs)

# Calculate the number of different sets of drinks
num_nights = 0
for i in range(1, n + 1):
    for j in range(i, n + 1):
        if not any((k, l) in bad_pairs for k in range(i, j+1) for l in range(i, j+1) if k != l):
            num_nights = (num_nights + 1) % (10**9 + 7)

print(num_nights)
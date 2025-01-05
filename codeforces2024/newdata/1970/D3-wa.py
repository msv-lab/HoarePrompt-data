import sys

# Read the number of magic words to create
n = int(input())

# Generate n distinct magic words
# The pattern used here is 'X' repeated i times followed by 'O' if i is odd
words = ['X' * i + 'O' * (i % 2) for i in range(1, n + 1)]

# Print the magic words, one per line
print('\n'.join(words))
sys.stdout.flush()

# Precompute the powers of all possible concatenations of magic words
powers = {}
for i in range(n):
    for j in range(n):
        # Concatenate the words and calculate the power
        concatenated = words[i] + words[j]
        power = len(set(concatenated[k:l] for k in range(len(concatenated)) for l in range(k + 1, len(concatenated) + 1)))
        # Store the power and the indices in the dictionary
        powers[power] = (i + 1, j + 1)

# Read the number of students (queries)
q = int(input())

# Process each query
for _ in range(q):
    # Read the power of the spell
    p = int(input())
    # Look up the power in the dictionary to find the indices
    u, v = powers[p]
    # Print the indices of the magic words
    print(u, v)
    sys.stdout.flush()
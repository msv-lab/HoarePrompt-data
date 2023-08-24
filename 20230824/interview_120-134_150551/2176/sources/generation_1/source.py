
# Read the input
n = int(input())

# Create two dictionaries to store the frequencies of each element for the first and second positions
freq_1 = {}
freq_2 = {}

# Iterate through the input and update the frequencies
for _ in range(n):
    a, b = map(int, input().split())
    freq_1[a] = freq_1.get(a, 0) + 1
    freq_2[b] = freq_2.get(b, 0) + 1

# Initialize the counts for bad sequences
count_1 = 1
count_2 = 1

# Iterate through the frequencies and calculate the counts for bad sequences
for freq in freq_1.values():
    count_1 *= freq
    count_1 %= 998244353

for freq in freq_2.values():
    count_2 *= freq
    count_2 %= 998244353

# Calculate the total number of permutations
total_permutations = pow(n, n, 998244353)

# Calculate the number of good permutations
good_permutations = (total_permutations - count_1 - count_2 + 998244353) % 998244353

# Print the result
print(good_permutations)

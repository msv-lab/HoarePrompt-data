n = int(input())
a = list(map(int, input().split()))

# Count the frequency of each number in the array
freq = {}
for num in a:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

# Calculate the expected number of unique elements
expected = 0
for i in range(1, n+1):
    expected += freq[i] / n

print('{:.6f}'.format(expected))
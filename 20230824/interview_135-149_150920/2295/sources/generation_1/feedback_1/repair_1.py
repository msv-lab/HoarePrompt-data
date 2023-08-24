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
total_pairs = n * (n+1) // 2
expected = 0
for i in range(n):
    expected += freq[a[i]] / total_pairs

print('{:.6f}'.format(expected))
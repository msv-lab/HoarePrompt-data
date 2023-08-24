n, m, k = map(int, input().split())
p = list(map(int, input().split()))

# Calculation of maximum sum

# Choosing k pairs with length m
pairs = [p[i:i+m] for i in range(0, n, m)]

# Handling the case where the number of valid pairs is less than k
if len(pairs) < k:
    max_sum = sum(sum(pair) for pair in pairs)
else:
    max_sum = sum(sum(pair) for pair in pairs[:k])

print(max_sum)
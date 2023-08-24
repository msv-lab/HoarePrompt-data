n, m, k = map(int, input().split())
p = list(map(int, input().split()))

# Sorting the sequence in descending order to consider the largest values first
p.sort(reverse=True) 

# Choosing k pairs with length m
pairs = [p[i:i+m] for i in range(0, n, m)]

# Calculating the maximum sum
max_sum = sum(sum(pair) for pair in pairs[:k])

print(max_sum)
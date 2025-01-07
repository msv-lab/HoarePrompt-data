n = int(input())

# The maximum number of nines at the end is determined by the largest factor of 10^i less than or equal to n
max_9s = 0
while (n + 1) % 10 == 0:
    max_9s += 1
    n //= 10

# For each i from 1 to 10^max_9s, there are (n // 10^max_9s) pairs (i, n - i) that sum to something ending with max_9s nines
pairs = (n + 1) * max_9s
print(pairs)

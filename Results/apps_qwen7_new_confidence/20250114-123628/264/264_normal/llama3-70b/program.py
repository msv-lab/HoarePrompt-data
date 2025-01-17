n = int(input())
m = int(input())
a = [int(input()) for _ in range(n)]

min_k = max(a) + (m + n - 1) // n
max_k = max(a) + m

print(min_k, max_k)

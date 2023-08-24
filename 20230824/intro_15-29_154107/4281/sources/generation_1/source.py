n = int(input())
x = list(map(int, input().split()))

x_set = set(x)

min_houses = len(x_set)

max_houses = max(min(x) - 1, n - max(x))
print(min_houses, max_houses)
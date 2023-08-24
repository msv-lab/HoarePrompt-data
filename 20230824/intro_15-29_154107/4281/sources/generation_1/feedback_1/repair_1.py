n = int(input())
x = list(map(int, input().split()))

min_houses = len(set(x))

max_houses = max(max(x) - min(x) + 1, n)
print(min_houses, max_houses)
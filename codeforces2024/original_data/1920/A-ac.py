t = int(input())
for _ in range(t):
    n = int(input())
    lower, upper = 0, float("inf")
    removals = []
    for i in range(n):
        a, x = map(int, input().split())
        if a == 1:
            lower = max(lower, x)
        elif a == 2:
            upper = min(upper, x)
        else:
            removals.append(x)
    counts = 0
    for num in removals:
        if lower <= num <= upper:
            counts += 1
    print(max(0, upper - lower + 1 - counts))
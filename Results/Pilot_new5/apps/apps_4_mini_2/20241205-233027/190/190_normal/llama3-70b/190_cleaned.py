n = int(input())
sticks = list(map(int, input().split()))
sticks.sort()
mid = sticks[n // 2]
cost = sum((abs(x - mid) for x in sticks))
t = mid
min_cost = cost
min_t = t
for i in range(mid - 1, 0, -1):
    cost = sum((min(abs(x - i), abs(x - (i + 1))) for x in sticks))
    if cost < min_cost:
        min_cost = cost
        min_t = i
for i in range(mid + 1, 101):
    cost = sum((min(abs(x - i), abs(x - (i - 1))) for x in sticks))
    if cost < min_cost:
        min_cost = cost
        min_t = i
print(min_t, min_cost)
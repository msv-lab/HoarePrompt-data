n, m = map(int, input().split())

day = 1
grains = n
while grains > 0:
    grains += m
    if grains > n:
        grains = n
    grains -= day
    day += 1

print(day - 1)

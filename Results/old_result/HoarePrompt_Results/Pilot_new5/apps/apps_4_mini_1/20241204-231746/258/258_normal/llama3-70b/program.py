import math

N, K = map(int, input().split())
meats = []
for _ in range(N):
    x, y, c = map(int, input().split())
    meats.append((x, y, c))

def distance(x, y, X, Y):
    return math.sqrt((X - x) ** 2 + (Y - y) ** 2)

def time_to_ready(x, y, X, Y):
    return [c * distance(x, y, X, Y) for x, y, c in meats]

def solve():
    ans = float('inf')
    for x in range(-1000, 1001):
        for y in range(-1000, 1001):
            times = time_to_ready(x, y, x, y)
            times.sort()
            ans = min(ans, times[K - 1])
    return ans

print(solve())

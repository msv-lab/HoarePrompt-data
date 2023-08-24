mod = 10**9 + 7

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

x_count = len(set(x for x, _ in points))
y_count = len(set(y for _, y in points))

result = pow(2, x_count + y_count, mod) - 1

print(result % mod)
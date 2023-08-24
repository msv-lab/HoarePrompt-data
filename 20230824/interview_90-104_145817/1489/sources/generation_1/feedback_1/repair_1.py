mod = 10**9 + 7

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

x_count = len(set(x for x, _ in points))
y_count = len(set(y for _, y in points))

result = pow(3, x_count + y_count, mod) # removed the subtraction of 1

print(result % mod)
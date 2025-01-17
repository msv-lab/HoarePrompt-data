n, m = map(int, input().split())
stars = []
for _ in range(n):
    row = input()
    for j, c in enumerate(row):
        if c == '*':
            stars.append((j, _))

min_x = min(x for x, y in stars)
max_x = max(x for x, y in stars)
min_y = min(y for x, y in stars)
max_y = max(y for x, y in stars)

side = max(max_x - min_x + 1, max_y - min_y + 1)
print(side)

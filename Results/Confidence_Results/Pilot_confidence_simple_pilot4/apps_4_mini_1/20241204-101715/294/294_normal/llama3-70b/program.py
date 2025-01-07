def count_squares(n, m):
    count = 0
    for i in range(1, min(n, m) + 1):
        count += (n - i + 1) * (m - i + 1)
    return count

x = int(input())
tables = []
for n in range(1, int(x ** 0.5) + 1):
    for m in range(n, int(x ** 0.5) + 1):
        if count_squares(n, m) == x:
            tables.append((n, m))
tables.sort()
print(len(tables))
for table in tables:
    print(table[0], table[1])

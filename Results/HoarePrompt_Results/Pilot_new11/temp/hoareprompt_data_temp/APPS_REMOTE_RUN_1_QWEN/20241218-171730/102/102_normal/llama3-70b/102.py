n = int(input())
a = int(input())
b = int(input())

for x in range(n // a + 1):
    y = (n - x * a) // b
    if x * a + y * b == n:
        print('YES')
        print(x, y)
        exit()

print('NO')

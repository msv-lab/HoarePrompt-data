a = int(input())
for i in range(a):
    (x, y) = map(int, input().split())
    z = (y + 1) // 2
    m = 15 * z - y * 4
    if m < a:
        z = z + (x - m + 15 - 1) // 15
    print(z)
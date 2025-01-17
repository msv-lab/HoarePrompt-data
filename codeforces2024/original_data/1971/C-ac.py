t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    if a > b:
        a, b = b, a
    if (a<c<b) ^ (a<d<b):
        print('YES')
    else:
        print('NO')
a = int(input())
for i in range(a):
    (b, c) = map(int, input().split())
    q = (b, c)
    if b == c:
        print('YES')
    elif b < c:
        print('NO')
    elif b % 2 == c % 2:
        print('Yes')
    else:
        print('No')
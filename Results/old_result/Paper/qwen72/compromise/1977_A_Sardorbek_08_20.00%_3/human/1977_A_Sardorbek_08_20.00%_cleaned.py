a = int(input())
for i in range(a):
    (b, c) = map(int, input().split())
    q = (b, c)
    if b == c:
        print('YES')
    elif b < c:
        print('NO')
    elif a % 2 == b % 2:
        print('Yes')
    else:
        print('No')
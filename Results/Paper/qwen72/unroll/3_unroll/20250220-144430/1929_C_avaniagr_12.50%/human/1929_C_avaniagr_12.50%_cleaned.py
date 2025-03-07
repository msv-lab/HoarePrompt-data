t = int(input())
for _ in range(t):
    (k, x, a) = map(int, input().split())
    if x < k - 1:
        if a >= x + 1:
            print('YES')
        else:
            print('NO')
    elif x == k - 1:
        if a >= x + 3:
            print('YES')
        else:
            print('NO')
    else:
        z = 0
        for i in range(x + 1):
            z += z // (k - 1) + 1
        if a >= z:
            print('YES')
        else:
            print('NO')
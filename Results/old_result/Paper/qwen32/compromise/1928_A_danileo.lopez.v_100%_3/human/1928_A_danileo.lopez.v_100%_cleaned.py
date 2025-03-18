t = int(input())
for _ in range(t):
    (a, b) = map(int, input().split())
    if a % 2 == 0 or b % 2 == 0:
        if a % 2 == 0:
            (a1, a2) = (a // 2, a // 2)
            if a1 != b:
                print('Yes')
                continue
        if b % 2 == 0:
            (b1, b2) = (b // 2, b // 2)
            if b1 != a:
                print('Yes')
                continue
        print('No')
    else:
        print('No')
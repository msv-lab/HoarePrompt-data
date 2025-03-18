for _ in range(int(input())):
    a = int(input())
    b = list(map(int, input().split()))
    for i in range(0, a - 2):
        if b[i] < 0:
            print('NO')
            break
        b[i + 1] -= b[i] * 2
        b[i + 2] -= b[i]
        b[i] -= b[i]
    else:
        if b[-1] != 0 or b[-2] != 0:
            print('NO')
        else:
            print('YES')
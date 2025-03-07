for _ in range(int(input())):
    a = int(input())
    b = list(map(int, input().split()))
    if b[0] % 2 == 1 and b[1] != b[0] + 2 or (b[-1] % 2 == 1 and b[-2] != b[-1] + 2):
        print('NO')
    else:
        print('YES')
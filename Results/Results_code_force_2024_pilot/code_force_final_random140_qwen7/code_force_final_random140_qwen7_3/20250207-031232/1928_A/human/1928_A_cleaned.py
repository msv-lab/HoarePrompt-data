n = int(input())
for i in range(n):
    (a, b) = [int(i) for i in input().split()]
    if a % 2 != 0 and b % 2 != 0:
        print('NO')
    elif a / 2 == b and b % 2 != 0 or (b / 2 == a and a % 2 != 0):
        print('NO')
    else:
        print('YES')
for _ in range(int(input())):
    (n, m) = map(int, input().split())
    if n < m:
        print('NO')
    elif n & 1 and m & 1 or (n % 2 == 0 and m % 2 == 0):
        print('YES')
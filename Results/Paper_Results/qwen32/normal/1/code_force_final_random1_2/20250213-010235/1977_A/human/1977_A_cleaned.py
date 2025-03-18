t = int(input())
for i in range(t):
    (n, m) = [int(i) for i in input().split()]
    if n == m:
        print('Yes')
    elif m > n:
        print('No')
    elif m == n - 1:
        print('Yes')
    elif m % 2 == 0 and n % 2 == 0:
        print('Yes')
    elif m % 2 != 0 and n % 2 != 0:
        print('Yes')
    else:
        print('No')
def func_1(n, m, k):
    if m == k or k > n:
        return 'NO'
    elif m > k:
        return 'YES'
    else:
        return 'NO'
for _ in range(int(input())):
    (n, m, k) = map(int, input().split())
    print(func_1(n, m, k))
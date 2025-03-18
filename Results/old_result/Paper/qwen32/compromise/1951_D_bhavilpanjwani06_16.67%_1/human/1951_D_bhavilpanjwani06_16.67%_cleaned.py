def func_1():
    (n, k) = map(int, input().split())
    if n < k:
        print('NO')
    elif n == k:
        print('YES')
        print(1)
        print(n)
    elif k - 1 < n - k + 1:
        print('YES')
        print(2)
        print(n - k + 1, 1)
    else:
        print('NO')
for _ in range(int(input())):
    func_1()
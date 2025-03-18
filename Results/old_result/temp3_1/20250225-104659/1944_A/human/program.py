t = int(input())
for _ in range(t):
    (n, k) = map(int, input().split())
    print(func_1(n, k))

def func_1(n, k):
    if k >= n - 1:
        return 1
    else:
        return n


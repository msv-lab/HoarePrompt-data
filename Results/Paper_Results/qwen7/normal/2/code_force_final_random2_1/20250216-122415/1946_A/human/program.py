'''Median of Array'''
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    p = (n + 1) // 2 - 1
    res = a.count(a[p])
    print(res)
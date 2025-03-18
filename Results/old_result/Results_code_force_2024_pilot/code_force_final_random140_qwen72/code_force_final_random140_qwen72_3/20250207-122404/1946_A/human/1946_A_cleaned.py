"""Median of Array"""
t = int(input())
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    a.sort()
    p = (n + 1) // 2 - 1
    res = a[p:].count(a[p])
    print(res)
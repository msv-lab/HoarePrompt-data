"""
Created on Fri Sep  6 21:42:15 2024
 
@author: dehon
"""
t = int(input())
for _ in range(t):
    (n, k, x) = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    ans1 = sum(a)
    for i in range(x):
        ans1 -= a[i] * 2
    ans2 = ans1
    for i in range(k):
        ans1 += a[i]
        if i + x < n:
            ans1 -= a[i + x] * 2
        ans2 = max(ans1, ans2)
    print(ans2)
# -*- coding: utf-8 -*-
"""
    @Time : 2024/8/26 17:59
    @Author : Zhiliang.L
    @Email : 2410103062@mails.edu.cn
    @File : 1955-C.py
"""
T = int(input())
while T:
    T -= 1
    n, k = input().split()
    n = int(n)
    k = int(k)
    a = input().split()
    a = list(map(lambda x: int(x), a))
    l = 0
    r = n - 1
    ans = 0
    while l < r and k > 0:
        mi = min(a[l], a[r])
        if mi * 2 <= k:
            a[l] -= mi
            a[r] -= mi
            k -= (mi * 2)
            if a[l] == 0:
                ans += 1
                l += 1
            if a[r] == 0:
                ans += 1
                r -= 1
        else:
            t = k % 2
            if a[l] - t - k // 2 == 0:
                ans += 1
            break
    if l == r:
        ans += (k >= a[l])
    print(ans)
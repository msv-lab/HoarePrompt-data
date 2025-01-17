R = lambda : map(int, input().split())
(t,) = R()
while t:
    t -= 1
    (n, k) = R()
    (*a,) = R()
    i = 0
    j = n - 1
    while i < j and (m := min(a[i], a[j], k // 2)):
        k -= m * 2
        a[i] -= m
        i += a[i] < 1
        a[j] -= m
        j -= a[j] < 1
    print(i + n - j - 1 + (k >= a[i] > 0))
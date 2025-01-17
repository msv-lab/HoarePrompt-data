def solve():
    n, m, k = map(int, input().split())
    a = [int(x) for x in input().split()]
    d = [int(x) for x in input().split()]
    f = [int(x) for x in input().split()]
    d.sort()
    f.sort()

    m1, m2 = 0, 0
    ind = -1
    for i in range(1, n):
        e = a[i] - a[i - 1]
        m2 = max(m2, e)
        if m2 > m1:
            m1, m2 = m2, m1
            ind = i - 1

    ans = m1

    target = (a[ind] + a[ind + 1]) // 2
    for model in d:
        l, r = 0, k - 1
        while r - l > 1:
            mid = (r + l) // 2
            if model + f[mid] <= target:
                l = mid
            else:
                r = mid
        ans = min(ans, max(m2, abs(model + f[l] - a[ind]), abs(model + f[l] - a[ind + 1])))
        ans = min(ans, max(m2, abs(model + f[r] - a[ind]), abs(model + f[r] - a[ind + 1])))
    print(ans)


for _ in range(int(input())):
    solve()
ans_list = []
for _ in range(int(input())):
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = a[0]
    res = n - 1
    for i in range(n - 1):
        dif = a[i + 1] - a[i]
        if dif == 0:
            res -= 1
        if dif != 0:
            if k >= dif * (i + 1):
                ans += dif
                k -= dif * (i + 1)
                res -= 1
            else:
                ans += k // (i + 1)
                if i != 0:
                    res += k % (i + 1)
                k = 0
                break
            if k == 0:
                break
    if k != 0:
        ans += k // n
        res += k % n
    ans += (ans - 1) * (n - 1)
    ans += res
    ans_list.append(ans)
for a in ans_list:
    print(a)
def func_1():
    (n, t) = (int(i) for i in input().split())
    a = [[int(i) for i in input().split()] for i in range(n)]
    'q = int(input())\n  while q:\n    l, r = map(int, input().split())\n    q -= 1\n    '
    a.sort(key=lambda x: x[1])
    ans = 0
    l = r = 0
    res = 0
    while r < n:
        res += a[r][0]
        if r > 0:
            res += a[r][1] - a[r - 1][1]
        while res > t:
            res -= a[l][0]
            if l < n - 1:
                res -= a[l + 1][1] - a[l][1]
            l += 1
        ans = max(ans, r - l + 1)
        r += 1
    return ans
t = int(input())
while t:
    print(func_1())
    t -= 1
def func_1(n, m, a, s):
    b = []
    l = 0
    r = n - 1
    for i in range(n):
        if s[i] == 'L':
            b.append(a[l])
            l += 1
        else:
            b.append(a[r])
            r -= 1
    ans = []
    p = 1
    for v in reversed(b):
        p = p * v % m
        ans.append(p)
    return reversed(ans)
for _ in range(int(input())):
    (n, m) = map(int, input().split())
    a = list(map(int, input().split()))
    s = input()
    print(*func_1(n, m, a, s))
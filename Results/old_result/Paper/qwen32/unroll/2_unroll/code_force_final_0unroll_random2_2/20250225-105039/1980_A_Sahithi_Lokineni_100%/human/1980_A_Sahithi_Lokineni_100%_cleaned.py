def func_1():
    return 0
t = int(input())
while t > 0:
    t -= 1
    d = defaultdict(default_value)
    (n, m) = list(map(int, input().split()))
    s = input()
    d['A'] = 0
    d['B'] = 0
    d['C'] = 0
    d['D'] = 0
    d['E'] = 0
    d['F'] = 0
    d['G'] = 0
    for i in range(n):
        d[s[i]] = d[s[i]] + 1
    ans = 0
    for val in d.keys():
        if d[val] <= m:
            ans = ans + m - d[val]
    print(ans)
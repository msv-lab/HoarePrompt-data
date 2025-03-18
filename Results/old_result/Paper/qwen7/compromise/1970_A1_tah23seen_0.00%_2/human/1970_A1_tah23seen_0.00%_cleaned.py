def func_1(s):
    n = len(s)
    ans = ''
    d = {}
    d[0] = 0
    for i in range(len(s)):
        if s[i] == '(':
            d[i + 1] = d[i] + 1
        else:
            d[i + 1] = d[i] - 1
    d.pop(n)
    d = sorted(d.items(), key=lambda x: x[1])
    for (i, j) in d:
        ans += s[i]
    return ans
n = input()
print(func_1(n))
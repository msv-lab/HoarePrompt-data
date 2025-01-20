def func_1(t):
    n = len(t)
    for i in range(1, n):
        if t[:i] == t[-i:]:
            s = t[:-i]
            if s + t[-i:] == t:
                return 'YES\n' + s
    return 'NO'
t = input().strip()
print(func_1(t))
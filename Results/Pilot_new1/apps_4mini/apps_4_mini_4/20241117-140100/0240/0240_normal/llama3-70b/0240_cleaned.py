s = input()
t = input()

def func_1(s, t):
    t_set = set(t)
    n = ''
    for c in s:
        if c in t_set:
            n += c
    n += t
    return int(n)
print(func_1(s, t))
s = input()
t = input()

def smallest_n(s, t):
    t_set = set(t)
    n = ''
    for c in s:
        if c in t_set:
            n += c
    n += t
    return int(n)

print(smallest_n(s, t))

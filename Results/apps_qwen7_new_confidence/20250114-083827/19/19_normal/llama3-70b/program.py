s = input()
t = ''
u = ''

while s or t:
    if s:
        t += s[0]
        s = s[1:]
    if t:
        u += min(t)
        t = t.replace(min(t), '', 1)

print(u)

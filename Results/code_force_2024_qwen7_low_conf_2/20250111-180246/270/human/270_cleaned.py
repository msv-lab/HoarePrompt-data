s = input()
q = [[]]
it = iter(q)
cur = next(it)
for c in s:
    if c == '(':
        x = []
        cur.append(x)
        q.append(x)
    if c == ')':
        cur = next(it)

def func_1(u):
    q = [(0, v) for v in u]
    s = []
    while q:
        (pc, u) = q.pop()
        if pc == 0:
            s.append('(')
            q.append((1, u))
            q.extend(((0, v) for v in u))
        if pc == 1:
            s.append(')')
    return ''.join(s)
print(func_1(q[0]))
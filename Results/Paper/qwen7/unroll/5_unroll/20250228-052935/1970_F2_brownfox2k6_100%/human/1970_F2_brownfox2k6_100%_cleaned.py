def func_1(obj, d):
    if d == 'U':
        obj[0] -= 1
    elif d == 'D':
        obj[0] += 1
    elif d == 'L':
        obj[1] -= 1
    elif d == 'R':
        obj[1] += 1

def func_2(t):
    out = []
    for p in player:
        if player[p] == blud:
            out.append(p)
            player[p] = [-1, -1]
    for p in sorted(out):
        print(t, p, 'ELIMINATED')
(n, m) = map(int, input().split())
rg = []
bg = []
blud = [-1, -1]
player = dict()
for i in range(n):
    s = input().split()
    for j in range(m):
        if s[j] == 'RG':
            rg.append([i, j])
        elif s[j] == 'BG':
            bg.append([i, j])
        elif s[j] == '.Q':
            ball = [i, j]
        elif s[j] == '.B':
            blud = [i, j]
        else:
            player[s[j]] = [i, j]
carry = None
bs = rs = 0
for t in range(int(input())):
    (p, d) = input().split()[:2]
    if d == 'C':
        carry = p
    elif d == 'T':
        carry = None
        if ball in bg:
            rs += 1
            print(t, 'RED GOAL')
            ball = [n // 2, m // 2]
        elif ball in rg:
            bs += 1
            print(t, 'BLUE GOAL')
            ball = [n // 2, m // 2]
    elif p == '.Q':
        func_1(ball, d)
    elif p == '.B':
        func_1(blud, d)
        func_2(t)
    else:
        func_1(player[p], d)
        func_2(t)
        if carry == p:
            ball = player[p]
print('FINAL SCORE:', rs, bs)
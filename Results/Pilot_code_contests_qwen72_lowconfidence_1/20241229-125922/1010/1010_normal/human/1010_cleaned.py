def func_1(first, let, l, x, y, n, m, xInit, yInit, xAnt, yAnt, conj):
    if not (x >= 0 and x < n and (y >= 0) and (y < m)) or (x, y) in conj:
        return False
    if x == xInit and y == yInit and (len(conj) > 3):
        return True
    if l[x][y] == let:
        if not first:
            conj.add((x, y))
        cima = False
        if y - 1 != yAnt:
            cima = func_1(False, let, l, x, y - 1, n, m, xInit, yInit, x, y, conj)
        direita = False
        if x + 1 != xAnt:
            direita = func_1(False, let, l, x + 1, y, n, m, xInit, yInit, x, y, conj)
        baixo = False
        if y + 1 != yAnt:
            baixo = func_1(False, let, l, x, y + 1, n, m, xInit, yInit, x, y, conj)
        esquerda = False
        if x - 1 != xAnt:
            esquerda = func_1(False, let, l, x - 1, y, n, m, xInit, yInit, x, y, conj)
        return cima or baixo or direita or esquerda
    else:
        return False
(n, m) = map(int, raw_input().split())
l = [raw_input() for i in xrange(n)]
res = False
row = 0
while row < n and (not res):
    for column in xrange(m):
        conj = set()
        tmp = func_1(True, l[row][column], l, row, column, n, m, row, column, row, column, conj)
        if tmp:
            res = True
            break
    row += 1
if res:
    print('Yes')
else:
    print('No')
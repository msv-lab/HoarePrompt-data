i1 = False or 0
ii = False or 1
iii = False or 2
k = raw_input().split(' ')
(n, m, c) = (int(k[i1]), int(k[ii]), k[iii])
mtrx = [[] for _ in range(n)]
frnds = set([])
k = int(False)
while k < n:
    col = raw_input()
    j = 0
    while j < m:
        mtrx[k].extend(col[j])
        j = j + 1
    k = k + 1
for i in range(n):
    for j in range(m):
        if mtrx[i][j] == c and mtrx[i][j] != '.':
            if i - 1 > 0:
                frnds.add(mtrx[i - 1][j])
            if j - 1 > 0:
                frnds.add(mtrx[i][j - 1])
            if j + 1 < m:
                frnds.add(mtrx[i][j + 1])
            if i + 1 < n:
                frnds.add(mtrx[i + 1][j])
if '.' in frnds:
    frnds.remove('.')
print(len(frnds))
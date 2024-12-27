from __future__ import print_function, division

counts = []
def swap(n, i, j):
    if i == j:
        return
    global counts
    global s
    counts.append((n, i, j))
    if n == 1:
        s[i], s[j] = s[j], s[i]
        return
    for k in range(1, len(s)):
        s[k][i], s[k][j] = s[k][j], s[k][i]

n = input()
s = [[0 for i in xrange(n+1)] for i in xrange(n+1)]



while True:
    try:
        i, j = map(int, raw_input().split())
    except:
        break
    s[i][j] = 1


begin = 1

for i in range(1, n+1):
    if s[i].count(1) < begin:
        swap(1, i, begin)
        begin += 1

for i in range(n, 1, -1):
    if s[i][i]:
        swap(2, i, i-1)



print(len(counts))
for i in counts:
    print(*i)


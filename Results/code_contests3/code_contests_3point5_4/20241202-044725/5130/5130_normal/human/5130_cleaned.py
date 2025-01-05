n = int(raw_input())
p = [int(v) - 1 for v in raw_input().split()]
b = map(int, raw_input().split())
comps = [0 for i in xrange(n)]
col = 0
for i in xrange(n):
    if comps[i] == 0:
        col += 1
        comps[i] = col
        j = i
        while comps[p[j]] == 0:
            j = p[j]
            comps[j] = col
print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
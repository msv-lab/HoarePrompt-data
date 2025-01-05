__author__ = 'Rikishi'

n = int(raw_input())
dyn = [[0] * 26 for i in range(26)]
for i in range(n):
    s = raw_input()
    first = ord(s[0]) - ord('a')
    last = ord(s[-1]) - ord('a')
    for j in range(26):
        if (dyn[j][first] > 0):
            dyn[j][last] = dyn[j][first] + len(s)
    dyn[first][last] = max(dyn[first][last], len(s))

ans = max([dyn[i][i] for i in range(26)])

print(ans)
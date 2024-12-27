from sys import stdin

rstr = lambda: stdin.readline().strip()
rint = lambda: int(stdin.readline())
rints = lambda: [int(x) for x in stdin.readline().split()]
rints_2d = lambda n: [rints() for _ in range(n)]
out = []
chrs = 'abcdefghijklmnopqrstuvwxyz'

s, n = rstr(), rint()
qur, mem = rints_2d(n), []
for i in chrs:
    tem = [0]
    for j in range(len(s)):
        tem.append(tem[-1] + (s[j] == i))
    mem.append(tem)

for l, r in qur:
    all = []
    for i in range(26):
        tem = mem[i][r] - mem[i][l - 1]
        if tem:
            all.append((tem, chrs[i]))

    out.append('Yes' if l == r or s[l - 1] != s[r - 1] or len(all) > 2 else 'No')
print('\n'.join(map(str, out)))

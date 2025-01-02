from sys import stdin

rints = lambda: [int(x) for x in stdin.readline().split()]
rstrs = lambda: [str(x) for x in stdin.readline().split()]

n, m = rints()
mem, ans = [[] for _ in range(m + 1)], []
for _ in range(n):
    a = rstrs()
    mem[int(a[1])].append((int(a[-1]), a[0]))

for i in range(1, m + 1):
    mem[i].sort()
    tem = mem[i]
    if len(tem) > 2 and tem[-3][0] in (tem[-1][0], tem[-2][0]):
        ans.append('?')
    else:
        ans.append('%s %s' % (tem[-1][1], tem[-2][1]))

print('\n'.join(ans))

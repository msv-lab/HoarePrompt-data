rstr = lambda : stdin.readline().strip()
rstrs = lambda : [str(x) for x in stdin.readline().split()]
rint = lambda : int(stdin.readline())
rints = lambda : [int(x) for x in stdin.readline().split()]
rstr_2d = lambda n: [rstr() for _ in range(n)]
rint_2d = lambda n: [rint() for _ in range(n)]
rints_2d = lambda n: [rints() for _ in range(n)]
pr = lambda args, sep: stdout.write(sep.join(map(str, args)) + '\n')
out = []
(n, ans) = (int(input()), 0)
for i in range(2, n + 1):
    cur = 2
    while i * cur <= n:
        ans += 4 * cur
        cur += 1
print(ans)
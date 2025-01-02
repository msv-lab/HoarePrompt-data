def func_1():
    return int(sys.stdin.readline())

def func_2():
    return map(int, sys.stdin.readline().split())

def func_3():
    return sys.stdin.readline()

def func_4(*args):
    for s in args:
        sys.stdout.write(str(s) + ' ')
    sys.stdout.write('\n')
INF = 2000000000
MOD = 10 ** 9 + 7
sys.setrecursionlimit(INF)
n = func_1()
ans = [[] for i in range(n)]
x = 1
start = 0
while x <= n ** 2:
    for i in range(start, start + n):
        ans[i % n].append(x)
        x += 1
    start += 1
for i in range(n):
    for j in range(n):
        ans[i][j] = str(ans[i][j])
for i in range(n):
    func_4(' '.join(ans[i]))
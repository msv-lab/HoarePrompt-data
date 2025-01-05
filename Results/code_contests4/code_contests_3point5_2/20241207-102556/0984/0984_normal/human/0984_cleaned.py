INF = 10 ** 9 + 7
OFFLINE = 0
sys.setrecursionlimit(INF)

def func_1():
    return int(sys.stdin.readline())

def func_2():
    return map(int, sys.stdin.readline().split())

def func_3():
    return sys.stdin.readline().rstrip()

def func_4(*args):
    for s in args:
        sys.stdout.write(str(s) + ' ')
    sys.stdout.write('\n')

def func_5(*args):
    for s in args:
        sys.stdout.write(str(s))
if OFFLINE:
    sys.stdin = open('fin.txt', 'r')
    sys.stdout = open('fout.txt', 'w')
n = func_1()
a = func_2()
m = max(a)
cnt = 0
res = 0
for i in range(n):
    if a[i] == m:
        cnt += 1
    else:
        cnt = 0
    res = max(cnt, res)
func_4(res)
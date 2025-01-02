raw_input = stdin.readline
pr = stdout.write
mod = 10 ** 9 + 7

def func_1():
    return int(raw_input())

def func_2():
    return map(int, raw_input().split())

def func_3(n):
    stdout.write(str(n) + '\n')

def func_4(arr):
    pr(' '.join(map(str, arr)) + '\n')

def func_5():
    return map(int, stdin.read().split())
range = xrange
n = func_1()
BITTree = [0] * (n + 1)

def func_6(i):
    s = 0
    i = i + 1
    while i > 0:
        s += BITTree[i]
        i -= i & -i
    return s

def func_7(i, v):
    i += 1
    while i <= n:
        BITTree[i] += v
        i += i & -i

def func_8(x):
    ret = 0
    sm = 0
    for i in range(21, -1, -1):
        pw = 1 << i
        if ret + pw <= n and sm + BITTree[ret + pw] <= x:
            ret += pw
            sm += BITTree[ret]
    return ret
l = func_2()
for i in range(n):
    func_7(i, i)
ans = [0] * n
for i in range(n - 1, -1, -1):
    ans[i] = func_8(l[i])
    func_7(ans[i], -ans[i])
func_4(ans)
"""input
8
3 3 4
10 20 30
5 5 5
2 4 3
1 1000000000 1000000000
1 1000000000 999999999
3 2 5
3 2 6
"""
debug = 1
readln = sys.stdin.readline

def func_1(s):
    sys.stdout.write(str(s))

def func_2(s):
    sys.stdout.write(str(s))
    sys.stdout.write('\n')

def func_3():
    return int(readln())

def func_4():
    return map(int, readln().split())

def func_5():
    return readln()

def func_6():
    return readln().split()

def func_7(*args):
    if debug:
        print(' '.join(map(str, args)))

def func_8(X):
    minX = min(X)
    maxX = max(X)
    return max(0, (maxX - minX - 2) * 2)
t = func_3()
for _ in xrange(t):
    X = func_4()
    func_2(func_8(X))
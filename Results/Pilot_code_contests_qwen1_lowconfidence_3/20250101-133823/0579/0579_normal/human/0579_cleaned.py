testing = len(sys.argv) == 4 and sys.argv[3] == 'myTest'
if testing:
    cmd = sys.stdout
    from time import time
    start_time = int(round(time() * 1000))
    input = open(sys.argv[1], 'r').readline
    readAll = open(sys.argv[1], 'r').read
    sys.stdout = open(sys.argv[2], 'w')
else:
    input = sys.stdin.readline
    readAll = sys.stdin.read

class InputData:

    def __init__(self):
        self.lines = readAll().split('\n')
        self.n = len(self.lines)
        self.ii = -1

    def input(self):
        self.ii += 1
        assert self.ii < self.n
        return self.lines[self.ii]
inputData = InputData()
input = inputData.input

def func_1():
    return int(input())

def func_2():
    return list(map(int, input().split()))

def func_3():
    return list(input())

def func_4():
    return input()

def func_5(l, sep='\n'):
    print(sep.join(l))

def func_6():
    (n, m, k) = func_2()
    a = func_2()
    b = func_2()
    cntA = Counter(a)
    cntB = Counter(b)
    ans = 0
    for i in xrange(k):
        ans += k - cntA[a[i]] - cntB[b[i]] + 1
    print(ans / 2)
for _ in xrange(func_1()):
    func_6()
if testing:
    sys.stdout = cmd
    print(int(round(time() * 1000)) - start_time)
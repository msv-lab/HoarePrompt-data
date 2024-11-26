testing = len(sys.argv) == 4 and sys.argv[3] == 'myTest'
if testing:
    cmd = sys.stdout
    from time import time
    start_time = int(round(time() * 1000))
    input = open(sys.argv[1], 'r').readline
    sys.stdout = open(sys.argv[2], 'w')
else:
    input = sys.stdin.readline

def func_1():
    return int(input())

def func_2():
    return list(map(int, input().split()))

def func_3():
    s = input()
    return list(s[:len(s) - 1])

def func_4():
    s = input()
    return s[:len(s) - 1]

def func_5(l):
    print(' '.join(map(str, l)))

def func_6(BITree, index):
    sum = 0
    while index > 0:
        sum += BITree[index]
        index -= index & -index
    return sum

def func_7(BITree, n, index, val):
    while index <= n:
        BITree[index] += val
        index += index & -index

def func_8(arr, n):
    invcount = 0
    maxElement = max(arr)
    BIT = [0] * (maxElement + 1)
    for i in range(1, maxElement + 1):
        BIT[i] = 0
    for i in range(n - 1, -1, -1):
        invcount += func_6(BIT, arr[i] - 1)
        func_7(BIT, maxElement, arr[i], 1)
    return invcount

def func_9():
    (n, k) = func_2()
    if n == k:
        return range(1, k + 1)
    if n == k + 1:
        return range(1, k + 1 - 2) + [k, k - 1]
    a = range(1, k + 1) + range(k - 1, 2 * k - n - 1, -1)
    maxInv = func_8(a, n)
    for i in xrange(2 * k - n, k):
        a[k - 1] = i
        a[k - 2] = k
        a[k] = k
        curInv = func_8(a, n)
        if curInv <= maxInv:
            ans = range(1, k + 1)
            ans[k - 1] = i
            ans[i - 1] = k
            return ans
if __name__ == '__main__':
    for _ in xrange(func_1()):
        print(func_9())
    if testing:
        sys.stdout = cmd
        print(int(round(time() * 1000)) - start_time)
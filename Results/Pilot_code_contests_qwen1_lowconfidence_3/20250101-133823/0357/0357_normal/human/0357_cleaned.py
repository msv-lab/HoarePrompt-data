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

def func_5(l, sep=' '):
    print(sep.join(map(str, l)))

def func_6(n):
    i = 1
    sq_n = n ** 0.5
    divs = []
    while i <= sq_n:
        if n % i == 0:
            divs.append(i)
            if n / i != i:
                divs.append(n / i)
        i = i + 1
    return sorted(divs)

def func_7(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def func_8(arr, x, low, high):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return (mid, mid)
        elif arr[mid] > x:
            return func_8(arr, x, low, mid - 1)
        else:
            return func_8(arr, x, mid + 1, high)
    else:
        return (high, low)
p = [False] * 21001
for i in xrange(1, 21001):
    p[i] = func_7(i)
primes = [i for (i, x) in enumerate(p) if x]

def func_9():
    d = func_1()
    i = func_8(primes, d + 1, 0, len(primes) - 1)[1]
    j = i + 1
    while primes[j] - primes[i] < d:
        j += 1
    print(primes[i] * primes[j])
if __name__ == '__main__':
    for _ in xrange(func_1()):
        func_9()
    if testing:
        sys.stdout = cmd
        print(int(round(time() * 1000)) - start_time)
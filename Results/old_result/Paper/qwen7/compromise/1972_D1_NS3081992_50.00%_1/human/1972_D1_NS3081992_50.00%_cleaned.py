p2D = lambda x: print(*x, sep='\n')

def func_1():
    return int(sys.stdin.buffer.readline())

def func_2():
    return map(int, sys.stdin.buffer.readline().split())

def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))

def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]

def func_5():
    return sys.stdin.buffer.readline().rstrip()

def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()

def func_7():
    return [int(i) for i in input().split()]

def func_8(rows):
    return [func_7() for _ in range(rows)]

def func_9():
    return input()

def func_10():
    return int(input())

def func_11():
    return input().split()

def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if len(d[da]) == 1:
        return 1
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
    rank[da - 1] = tmp + 1
    return tmp + 1

def func_13(a, b):
    if b == 0:
        x = 1
        y = 0
        return (x, y, a)
    (x, y, g) = func_13(b, a % b)
    return (y, x - a // b * y, g)

def func_14(a, n, m, k):
    for i in range(n):
        if a[i] < m:
            k -= m - a[i]
    if k >= 0:
        return 1
    return -1

def func_15():
    (n, m) = func_7()
    i = 1
    ans = 0
    while i * i <= n + i:
        ans += (n + i) // (i * i)
        i += 1
    return ans - 1

def func_16():
    for _ in range(func_10()):
        sys.stdout.write(str(func_15()) + '\n')
if __name__ == '__main__':
    func_16()
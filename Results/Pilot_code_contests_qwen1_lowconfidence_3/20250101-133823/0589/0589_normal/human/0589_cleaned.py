sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
sys.stdout = BytesIO()
register(lambda : os.write(1, sys.stdout.getvalue()))
input = lambda : sys.stdin.readline().rstrip('\r\n')

def func_1():
    return int(input())

def func_2():
    return list(map(int, input().split()))

def func_3():
    s = input()
    return list(s[:len(s)])

def func_4():
    return map(int, input().split())

def func_5(a, b):
    while a % b > 0:
        c = a % b
        a = b
        b = c
    return b

def func_6(l, r):
    for a in range(l, r + 1):
        for b in range(a + 1, r + 1):
            if func_5(r, b) == 1 and func_5(b, a) != 1:
                return (a, b, r)
    return (-1, -1, -1)
(l, r) = func_2()
if func_5(r, l) == 1:
    (a, b, c) = func_6(l, r)
    if a == -1:
        sys.stdout.write('-1\n')
    sys.stdout.write(str(a) + ' ' + str(b) + ' ' + str(c) + '\n')
else:
    sys.stdout.write(str(l) + ' ' + str(l + 1) + ' ' + str(r) + '\n')
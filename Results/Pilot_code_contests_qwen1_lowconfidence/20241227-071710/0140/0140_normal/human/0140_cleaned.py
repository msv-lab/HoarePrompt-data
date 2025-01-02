w = sys.stdout.write
read = sys.stdin.readline
reads = sys.stdin.read

def func_1(f=None):
    if f:
        return map(f, read().split())
    else:
        return read().split()

def func_2(t, f=None):
    result = []
    result_append = result.append
    for i in xrange(t):
        if f:
            result_append(tuple(map(f, read().split())))
        else:
            result_append(list(read().split()))
    return result
sqrt = math.sqrt
[n] = func_1(int)
xs = func_1(int)
xss = set(xs)
if n <= 2:
    w('-1')
    sys.exit()
if len(xss) == 1:
    w('-1')
    sys.exit()
if len(xs) == 3 and xs[0] == xs[2]:
    w('-1')
    sys.exit()

def func_3(xs, k):
    k2 = 0
    k1 = 0
    for i in xrange(0, n - 1, 1):
        if xs[i] < xs[i + 1]:
            k2 += 1
        if xs[i] > xs[i + 1]:
            k1 += 1
    if k2 >= 2:
        for i in xrange(0, n - 1, 1):
            if xs[i] < xs[i + 1]:
                w('%s %s' % (abs(i + 1 + k), abs(i + 2 + k)))
                sys.exit()
    if k2 == 1 and k1 >= 1 and (len(xss) < n):
        for i in xrange(0, n - 1, 1):
            if xs[i] > xs[i + 1]:
                w('%s %s' % (abs(i + 1 + k), abs(i + 2 + k)))
                sys.exit()
            if xs[i] < xs[i + 1]:
                w('%s %s' % (abs(i + 1 + k), abs(i + 2 + k)))
                sys.exit()
    if k2 == 1 and k1 == 0 and (len(xs) >= 3):
        for i in xrange(0, n - 1, 1):
            if xs[i] < xs[i + 1]:
                w('%s %s' % (abs(i + 1 + k), abs(i + 2 + k)))
                sys.exit()
    if k2 == 0:
        for i in xrange(0, n - 1, 1):
            if xs[0] != xs[i]:
                w('%s %s' % (abs(1 + k), abs(i + 1 + k)))
                sys.exit()
func_3(xs, 0)
xs.reverse()
func_3(xs, -1 * n)
w('-1')
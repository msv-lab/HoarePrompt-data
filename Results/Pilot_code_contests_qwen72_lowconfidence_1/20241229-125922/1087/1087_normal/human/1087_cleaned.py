input = sys.stdin
output = sys.stdout

def func_1(t):
    (a, b, c) = t
    D2 = [a + b, a + c, b + c]
    for d2 in D2:
        for d in t:
            if d2 == d:
                return 'SEGMENT'
            elif d2 < d:
                return None
    return 'TRIANGLE'

def func_2(D):
    for t in combinations(D, 3):
        r = func_1(t)
        if r is not None:
            return r
    return 'IMPOSSIBLE'

def func_3(d=' '):
    return [int(s) for s in input.readline().strip().split(d) if len(s.strip()) > 0]
D = func_3()
a = func_2(D)
output.write('%s\n' % a)
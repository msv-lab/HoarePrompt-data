sys.setrecursionlimit(100000)
if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from io import StringIO as stream
if sys.version_info[0] < 3:

    class dict(dict):
        """dict() -> new empty dictionary"""

        def items(self):
            """D.items() -> a set-like object providing a view on D's items"""
            return dict.iteritems(self)

        def keys(self):
            """D.keys() -> a set-like object providing a view on D's keys"""
            return dict.iterkeys(self)

        def values(self):
            """D.values() -> an object providing a view on D's values"""
            return dict.itervalues(self)
    input = raw_input
    range = xrange
    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

def func_1(sync=True):
    """Set whether the standard Python streams are allowed to buffer their I/O.
 
    Args:
        sync (bool, optional): The new synchronization setting.
 
    """
    global input, flush
    if sync:
        flush = sys.stdout.flush
    else:
        sys.stdin = stream(sys.stdin.read())
        input = lambda : sys.stdin.readline().rstrip('\r\n')
        sys.stdout = stream()
        register(lambda : sys.__stdout__.write(sys.stdout.getvalue()))

def func_2():
    return map(int, input().split())

def func_3():
    return list(map(int, input().split()))

def func_4(X, Y):
    return [x for (_, x) in sorted(zip(Y, X))]

def func_5():
    n = int(input())
    ar = func_3()
    ans = []
    for i in range(n - 1):
        if ar[i] % ar[i + 1] == 0 or ar[i + 1] % ar[i] == 0:
            ans.append(ar[i])
        elif ar[i] < ar[i + 1]:
            ans.append(ar[i])
            ar[i + 1] -= ar[i + 1] % ar[i]
        else:
            ans.append(ar[i])
            ar[i + 1] += ar[i + 1] % ar[i]
    ans.append(ar[i + 1])
    for i in ans:
        print(i, end=' ')
    print()

def func_6():
    testCase = 1
    if testCase:
        for _ in range(int(input())):
            func_5()
    else:
        func_5()
if __name__ == '__main__':
    func_1(False)
    func_6()
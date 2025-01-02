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
    return list(map(int, input().split()))

def func_3():
    return map(int, input().split())

def func_4():
    n = int(input())
    ar = func_2()
    for _ in range(int(input())):
        (a, b) = func_3()
        if a - 2 >= 0 and a - 2 < n:
            ar[a - 2] += b - 1
        if a >= 0 and a < n:
            ar[a] += ar[a - 1] - b
        ar[a - 1] = 0
    for i in ar:
        print(i)
if __name__ == '__main__':
    func_1(False)
    func_4()
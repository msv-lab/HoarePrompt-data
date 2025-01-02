"""
________        _____________              ______
___  __ \\____  ____  __ \\__(_)__   _______ ___  /
__  /_/ /_  / / /_  /_/ /_  /__ | / /  __ `/_  /
_  ____/_  /_/ /_  _, _/_  / __ |/ // /_/ /_  /
/_/     _\\__, / /_/ |_| /_/  _____/ \\__,_/ /_/
        /____/

https://github.com/Cheran-Senthil/PyRival
Copyright (c) 2018 Cheran Senthilkumar
"""
if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from io import StringIO as stream
if sys.version_info[0] < 3:

    class dict(dict):

        def items(self):
            return dict.iteritems(self)

        def keys(self):
            return dict.iterkeys(self)

        def values(self):
            return dict.itervalues(self)
    input = raw_input
    range = xrange
    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

def func_1(sync=True):
    """
    Sets whether the standard Python streams are allowed to buffer their I/O.

    Parameters
    ----------
    sync : bool, optional
        The new synchronization setting. Default is True.
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
    (n, m) = map(int, input().split(' '))
    if n > m:
        print('YES')
    else:
        a = list(map(lambda x: int(x) % m, input().split(' ')))
        dp = [[False] * m for _ in range(n)]
        dp[0][a[0]] = True
        for i in range(1, n):
            dp[i][a[i]] = True
            for (j, flag) in enumerate(dp[i - 1]):
                if flag:
                    dp[i][j] = True
                    dp[i][(j + a[i]) % m] = True
        if dp[-1][0]:
            print('YES')
        else:
            print('NO')
if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    func_1(False)
    func_2()
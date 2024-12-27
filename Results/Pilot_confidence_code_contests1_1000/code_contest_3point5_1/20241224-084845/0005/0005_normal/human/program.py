from sys import stdin
from collections import *


def fast2():
    import os, sys, atexit
    from cStringIO import StringIO as BytesIO
    # range = xrange
    sys.stdout = BytesIO()
    atexit.register(lambda: os.write(1, sys.stdout.getvalue()))
    return BytesIO(os.read(0, os.fstat(0).st_size)).readline


class order_tree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [[0, 0] for _ in range(self.n * 2)]
        self.order = defaultdict(int, {arr[i]: i for i in range(self.n)})

    # get interval[l,r)
    def query(self, l):
        res, coun = 0, 0
        l = self.order[l] + self.n
        r = self.n * 2

        while l < r:
            if l & 1:
                res += self.tree[l][0]
                coun += self.tree[l][1]
                l += 1

            if r & 1:
                r -= 1
                res += self.tree[r][0]
                coun += self.tree[r][1]

            l >>= 1
            r >>= 1

        return res, coun

    def update(self, ix, val):
        ix = self.n + self.order[ix]

        # set new value
        self.tree[ix][0] += val
        self.tree[ix][1] += 1

        # move up
        while ix > 1:
            self.tree[ix >> 1][0] = self.tree[ix][0] + self.tree[ix ^ 1][0]
            self.tree[ix >> 1][1] = self.tree[ix][1] + self.tree[ix ^ 1][1]
            ix >>= 1


input = fast2()
rints = lambda: [int(x) for x in input().split()]
n, a = int(input()), sorted(map(lambda x, y: [x, y], rints(), rints()))
dis = sorted(set([x[1] for x in a]))
tree, ans = order_tree(dis), 0

for i in range(n - 1, -1, -1):
    su, coun = tree.query(a[i][1])
    ans += su - coun * a[i][0]
    tree.update(a[i][1], a[i][0])

print(ans)

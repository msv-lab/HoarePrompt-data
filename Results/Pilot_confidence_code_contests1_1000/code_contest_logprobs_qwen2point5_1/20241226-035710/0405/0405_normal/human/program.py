from sys import stdin
from bisect import *


class segmenttree:
    def __init__(self, arr, n):
        self.tree, self.n = [0] * (2 * n), n
        # build tree
        if arr:
            for i in range(2 * n - 1, 0, -1):
                if i >= n:
                    self.tree[i] = arr[i - n]
                else:
                    self.tree[i] = max(self.tree[i << 1], self.tree[(i << 1) + 1])

    # get interval[l,r)
    def query(self, l, r):
        res = 0
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                res = max(self.tree[l], res)
                l += 1

            if r & 1:
                r -= 1
                res = max(self.tree[r], res)

            l >>= 1
            r >>= 1

        return res

    def update(self, ix, val):
        ix += self.n

        # set new value
        self.tree[ix] = val

        # move up
        while ix > 1:
            self.tree[ix >> 1] = max(self.tree[ix], self.tree[ix ^ 1])
            ix >>= 1


rints = lambda: [int(x) for x in stdin.readline().split()]
n, a, tree = int(input()), rints(), segmenttree([], 10 ** 5 + 1)

for i in range(n):
    val = tree.query(0, a[i])
    tree.update(a[i], val + 1)

print(tree.query(0, n + 1))

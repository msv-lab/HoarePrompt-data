from sys import stdin
from collections import *
from bisect import *


def arr_inp(n):
    if n == 1:
        return [int(x) for x in stdin.readline().split()]
    elif n == 2:
        return [float(x) for x in stdin.readline().split()]
    else:
        return list(stdin.readline()[:-1])


class segmenttree:
    def __init__(self, arr, n):
        self.tree, self.n, self.map1 = [0] * (2 * n), n, defaultdict(int)
        # build tree
        if arr:
            for i in range(2 * n - 1, 0, -1):
                if i >= n:
                    self.tree[i] = arr[i - n][1]
                    self.map1[arr[i - n][0]] = i
                else:
                    self.tree[i] = self.tree[i << 1] + self.tree[(i << 1) + 1]

    # get interval[l,r)
    def query(self, l, r):
        res = 0
        # l += self.n
        # r += self.n
        while l < r:
            if l & 1:
                res += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                res += self.tree[r]
            l >>= 1
            r >>= 1

        return res

    def update(self, ix, val):
        # ix += self.n
        # set new value
        self.tree[ix] = val
        # move up
        while ix > 1:
            self.tree[ix >> 1] = self.tree[ix] + self.tree[ix ^ 1]
            ix >>= 1


n, a, b, mem = int(stdin.readline()), arr_inp(1), arr_inp(1), defaultdict(int)
for i in range(n):
    mem[a[i] - b[i]] += 1

tree = segmenttree(sorted(mem.items(), key=lambda x: x[0]), len(mem.values()))
dis, ans, ext = set(), 0, 0 if min(mem.keys()) >= 0 else -(min(mem.keys()))

for i, j in mem.items():
    dis.add(ext + i)

for i in range(n):
    val = a[i] - b[i]
    mem[val] -= 1

    if not mem[val]:
        dis.discard(val + ext)

    tree.update(tree.map1[val], mem[val])
    ix = bisect_right(list(dis), max(-(val - 1) + ext, 0))

    if ix != len(dis):
        if ix > 0 and list(dis)[ix - 1] == max(-(val - 1) + ext, 0):
            ix -= 1
        ans += tree.query(tree.map1[list(dis)[ix] - ext], tree.map1[list(dis)[-1] - ext] + 1)
    # print(ix, dis, ans, max(-(val - 1) + ext, 0))
print(ans)

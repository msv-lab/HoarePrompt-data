# Author: Mak Kader
# Description: Template for pypy or python


import math
import sys
import heapq
from collections import defaultdict
from collections import deque
from sys import stdin, stdout
sys.setrecursionlimit(1 << 29)
# Flush output: sys.stdout.flush()

def readInts():
    return [int(x) for x in stdin.readline().split()]

def readInt():
    return int(stdin.readline())

def readLine():
    return stdin.readline().strip()

# template end


N = readInt()
#assert(N < 10000)

op = [0] + readInts()
pa = [0, 0] + readInts()

G = defaultdict(list)
for i in range(2, N + 1):
    p = pa[i]
    G[p].append(i)
nleaf = [0] * (N + 1)
for i in range(N, 0, -1):
    if len(G[i]) == 0:
        nleaf[i] = 1
        continue
    for j in G[i]:
        nleaf[i] += nleaf[j]  # if len(G[j]) > 0 else 1

memo = {}
def dfs(root):
    global memo
    if len(G[root]) == 0:
        return 1
    if root in memo:
        return memo[root]
    res = 0
    if op[root] == 0:  # min
        #nl = nleaf[root]

        for v in G[root]:
            res = max(res, dfs(v))

    else:
        # max node
        nl = nleaf[root]

        for v in G[root]:
            nlv = nleaf[v]
            res = max(res, nl - (nlv - dfs(v)))
    memo[root] = res
    return memo[root]


for i in range(N, 0, -1):
    dfs(i)

# print(memo)
res = dfs(1)
#print(nleaf[1] - ms, ms)
print(res)

from sys import stdin
from itertools import combinations, permutations

rints = lambda: [int(x) for x in stdin.readline().split()]
Max = 10001
n, k = rints()
a, mem, ans, msk = rints(), [0] * (Max * 10), 0, []
for i in a:
    mem[i] += 1

if not k:
    print(sum([i * (i - 1) // 2 for i in mem]))
    exit()

for com in combinations(range(14), k):
    cur = ['0'] * 14
    for i in com:
        cur[i] = '1'
    msk.append(int(''.join(cur), 2))

for i in range(Max):
    for j in msk:
        ans += mem[i ^ j] * mem[i]

print(ans >> 1)

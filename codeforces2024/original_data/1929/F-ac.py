import sys

# Constants
MX = 5 * 10 ** 5
MOD = 998244353

# Combinatorics class to handle factorials and combinations
class Combinatorics:
    def __init__(self, MX):
        # Precompute factorials and their inverses
        self.f = [1] * (MX + 1)
        self.g = [1] * (MX + 1)
        for i in range(2, MX + 1):
            self.f[i] = self.f[i - 1] * i % MOD
        self.g[-1] = pow(self.f[-1], -1, MOD)
        for i in range(MX, 1, -1):
            self.g[i - 1] = self.g[i] * i % MOD

    def fact(self, n):
        return self.f[n]

    def fact_inv(self, n):
        return self.g[n]

    def comb(self, n, m):
        # Calculate combination nCm
        res = 1
        for x in range(n, n - m, -1):
            res = res * x % MOD
        return (res * self.fact_inv(m)) % MOD

# Initialize combinatorics
Comb = Combinatorics(MX)

def solve():
    input = lambda: sys.stdin.readline().rstrip()
    n, C = map(int, input().split())
    l_son = [None] * (n + 1)
    r_son = [None] * (n + 1)
    vals = [None] * (n + 1)
    
    # Read the tree structure and values
    for i in range(1, n + 1):
        L, R, val = map(int, input().split())
        l_son[i] = L if L > 0 else None
        r_son[i] = R if R > 0 else None
        vals[i] = val
    
    # In-order traversal to collect values
    stack = []
    nums = [1]  # Start with a minimum value
    node = 1
    while node or stack:
        while node:
            stack.append(node)
            node = l_son[node]
        node = stack.pop()
        nums.append(vals[node])
        node = r_son[node]
    nums.append(C)  # End with the maximum value
    
    # Calculate the number of suitable BSTs
    res = 1
    l = -1
    for r in range(n + 2):
        if nums[r] > 0:
            if l != -1:
                # Calculate combinations for the segment
                res *= Comb.comb(nums[r] - nums[l] + r - l - 1, r - l - 1)
                res %= MOD
            l = r
    print(res)

# Read number of test cases
T = int(input())
for _ in range(T):
    solve()
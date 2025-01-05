#State of the program right berfore the function call: n, m, b are integers such that 1 ≤ n, m ≤ 500, 0 ≤ b ≤ 500; mod is a positive integer such that 1 ≤ mod ≤ 10^9 + 7; a is a list of n non-negative integers where each element ai satisfies 0 ≤ ai ≤ 500.
def func():
    add = lambda a, b: (a + b) % mod
    mult = lambda a, b: a % mod * (b % mod) % mod
    rints = lambda : [int(x) for x in stdin.readline().split()]
    n, m, b, mod = rints()
    a, mem = rints(), [[[int(j == 0) for _ in range(b + 1)] for j in range(m + 
    1)] for _ in range(2)]
    ans = 0
    for i in range(1, n + 1):
        ix = i & 1
        
        for j in range(1, m + 1):
            for k in range(a[i - 1], b + 1):
                mem[ix][j][k] = mem[ix ^ 1][j][k]
                mem[ix][j][k] = add(mem[ix][j][k], mem[ix][j - 1][k - a[i - 1]])
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `ans` is 0, `ix` is equal to `n % 2`, `mem` contains the final cumulative updates for all `j` from 1 to `m` and for all `k` from `a[i - 1]` to `b`.
    for i in range(b + 1):
        ans = add(ans, mem[n & 1][m][i])
        
    #State of the program after the  for loop has been executed: `ans` is the sum of `mem[n & 1][m][0]` to `mem[n & 1][m][b]`, `ix` is equal to `n % 2`, `n` is a positive integer, `mem` contains values.
    print(ans)
#Overall this is what the function does:The function accepts integers `n`, `m`, `b`, and a positive integer `mod`, along with a list `a` of non-negative integers. It computes a cumulative count based on the values in list `a`, where the count of ways to obtain sums from `0` to `b` using exactly `m` elements is stored in `mem`. The final result, which is the total number of ways to achieve these sums modulo `mod`, is printed.


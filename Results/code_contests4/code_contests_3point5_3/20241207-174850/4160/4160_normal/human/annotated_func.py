#State of the program right berfore the function call: n, m, b, mod are positive integers such that 1 <= n, m <= 500, 0 <= b <= 500, 1 <= mod <= 109 + 7. ai (bug count per line for each programmer) are non-negative integers such that 0 <= ai <= 500.
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
        
    #State of the program after the  for loop has been executed: `ix` is 1, `j` is `m`, `m` is greater than or equal to 1, `a[i - 1]` is a valid index, `b` is a valid value, `k` ranges from `a[i - 1]` to `b`, `mem[ix][j][k]` contains the final result after all iterations of the loop have executed
    for i in range(b + 1):
        ans = add(ans, mem[n & 1][m][i])
        
    #State of the program after the  for loop has been executed: `ix` is 1, `j` is `m`, `m` is greater than or equal to 1, `a[i - 1]` is a valid index, `b` is a valid value, `i` is equal to `b + 1`, `k` ranges from 0 to `b`, `mem[ix][j][k]` contains the final result after all iterations of the loop have executed, `ans` is the sum of all `mem[n & 1][m][i]` for i ranging from 0 to b
    print(ans)
#Overall this is what the function does:The function `func` does not accept any parameters. It initializes certain variables based on the provided constraints and performs calculations within nested loops. The function aims to calculate and print a result based on the final values stored in the `mem` array. The functionality does not specify a return value, and the final output is printed to the console. The code operates within the given constraints and performs calculations based on the iterations of the loops.


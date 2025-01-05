#State of the program right berfore the function call: n, m, b, and mod are all positive integers such that 1 ≤ n, m ≤ 500, 0 ≤ b ≤ 500, and 1 ≤ mod ≤ 10^9 + 7. The list a contains n non-negative integers where each integer is less than or equal to 500.**
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
        
    #State of the program after the  for loop has been executed: `ans` will have its final value after the loop executes. All values of `mem` will be updated based on the operations inside the loop for all valid values of `k` within the specified range. `ix` will be 1, `j` will be `m + 1`, `m` will be greater than or equal to 1, `a[i - 1]` will be a valid index in list `a`, `b` will be within the range of `a[i - 1]` up to `b + 1`, `n` will be at least 1.
    for i in range(b + 1):
        ans = add(ans, mem[n & 1][m][i])
        
    #State of the program after the  for loop has been executed: Output State: `ans` will be the sum of all values in `mem[n & 1][m][i]` for valid values of `i` within the range of `b + 1` for all iterations of the loop. All other variables maintain their initial conditions.
    print(ans)
#Overall this is what the function does:The function calculates a value based on the elements in the list `a`, the values of `m`, `b`, and `mod`. It updates the `mem` list based on certain conditions. Finally, it prints the sum of specific elements within `mem` with modulo operations applied. The function does not accept any parameters explicitly.


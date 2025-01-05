#State of the program right berfore the function call: **
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
        
    #State of the program after the  for loop has been executed: After all iterations of the loop have finished, `mem[ix][j+1][k]` will contain the final updated values based on the calculations performed within the loop. The values of `n`, `m`, `b`, `mod`, `a`, `ix`, `i`, `j`, and `k` will be determined by the loop conditions and the number of iterations. The loop will update `mem[ix][j+1][k]` for all values of `k` in the range from `a[n]` to `b` for each value of `j` in the range from 1 to `m`.
    for i in range(b + 1):
        ans = add(ans, mem[n & 1][m][i])
        
    #State of the program after the  for loop has been executed: The final updated values in `mem[ix][j+1][a[n]]` to `mem[ix][j+1][b]` will contain the final updated values after all iterations of the loop.
    print(ans)
#Overall this is what the function does:The function `func` defines lambda functions for addition, multiplication, and reading integers from input. It then reads values for `n`, `m`, `b`, and `mod` from input. It initializes arrays `a` and `mem` based on the input values. The function then performs calculations using nested loops to update `mem`. The final result is computed and printed. The function does not accept any parameters and does not return any value.


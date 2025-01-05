#State of the program right berfore the function call: **Precondition**: **N is an integer such that 1 <= N <= 21. For each i, j (1 <= i, j <= N), a_{i, j} is an integer 0 or 1.**
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: `MOD` is 1000000007, `n` is greater than 0, `a` is a list containing the result of mapping integers from input split by space for each iteration from 1 to `n`, `_` is assigned the value of `n` after the loop has executed
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: `MOD` is 1000000007, `n` is greater than 0, `a` contains mapped integers from input, `_` is (1 << n) - 1, `dp` is a 2D list with all values in the first row set to 1 and all other values set to 0
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: After all iterations of the loop have finished, the `dp` 2D list will contain updated values based on the provided formula. The values of `MOD`, `n`, `a`, `_`, `i`, and `mask` will remain unchanged.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:The function `func` reads input, processes it according to a specific algorithm, and prints the result. It initializes a 2D list `dp`, performs calculations based on the input values, and prints the final result. The function does not accept any parameters, and the output is printed to the console.


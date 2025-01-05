#State of the program right berfore the function call: N is an integer such that 1 <= N <= 21, and a_{i, j} is either 0 or 1 for all i and j where 1 <= i, j <= N.**
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: MOD is 1000000007, `n` is greater than 0, `a` contains `n` elements after the loop execution, each element of `a` is a list of integers obtained by mapping the integer conversion to the input split by space
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: `MOD` is 1000000007, `n` is greater than 0, `a` contains `n` elements, `dp` is a 2D list where each row has `(1 << n)` elements initialized to 0, for all values of `i` in the range of `(1 << n)`, `dp[0][i]` is assigned the value 1
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: MOD is 1000000007, n is greater than 0, a contains n elements, dp is a fully updated 2D list with all values calculated based on the loop conditions. Each dp[i][mask] value represents the final result of the calculations performed in the loop for all valid combinations of i and mask. The loop has iterated through all possible combinations of i and mask, updating dp[i][mask] according to the given conditions for all iterations.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:The function `func` reads an integer `n` as input and a 2D list `a` of size `n x n`. It then performs a series of calculations on the elements of `a` based on the binary representation of `n`. Finally, it prints the result of the calculations stored in a 2D list `dp` at the specific index `dp[n][(1 << n) - 1]`. The function operates within constraints specified for `n` and `a_{i, j}`, and the calculations involve bitwise operations and modular arithmetic.


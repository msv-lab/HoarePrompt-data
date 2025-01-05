#State of the program right berfore the function call: N is an integer such that 1 <= N <= 21 and a_{i,j} is either 0 or 1 for all i,j where 1 <= i,j <= N.**
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: MOD is assigned the value 1000000007, `n` is greater than 0, `_` is equal to n-1, `a` is a list containing n lists, each containing integers obtained by mapping `int` over the input split by spaces
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `_` is equal to n-1, `a` is a list containing n lists of integers, `dp` is a 2D list where dp[0][i] is assigned 1 for every i in the range 1 << n
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: Output State: `dp[i][mask]` has been updated for all valid values of `i`, `mask`, and `j` based on the conditions specified in the loop code. The final values of `dp[i][mask]` will be calculated by updating it with the previous value of `dp[i - 1][mask ^ 1 << j]` modulo `MOD` for all valid values of `mask` and `j`. The other variables `n`, `_`, `a`, and `MOD` will remain the same as in the initial state.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:The function `func` processes a matrix of size N x N, where N is an integer such that 1 <= N <= 21, and each element a_{i,j} of the matrix is either 0 or 1 for all i,j where 1 <= i,j <= N. The function initializes a dynamic programming array, updates its values based on specific conditions using bitwise operations, and finally prints a specific value from the array. The function does not accept any parameters and does not return any specific value.


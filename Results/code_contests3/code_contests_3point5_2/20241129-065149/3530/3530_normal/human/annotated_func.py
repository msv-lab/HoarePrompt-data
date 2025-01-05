#State of the program right berfore the function call: N is a positive integer. The input matrix a has dimensions N x N, where each value is either 0 or 1.**
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: Output State: N is a positive integer, `a` has dimensions N x N with each value being either 0 or 1, MOD is 1000000007, n is the input value, `a` is a list of N lists each containing integers from the input, _ is n-1. The loop appends a total of N lists to `a` with integers obtained by mapping the input values after splitting.
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: N is a positive integer, `a` has dimensions N x N with each value being either 0 or 1, MOD is 1000000007, n is the input value, `a` is a list of N lists each containing integers from the input, _ is n-1, `dp` is a 2D list initialized with 0 values of dimensions (n + 1) x (1 << n), all elements in dp[0] are assigned the value 1
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: At the end of the loop, `dp[n][mask]` holds the necessary computations modulo MOD for all combinations of n and mask. All other variables maintain their initial values, `n` is greater than 0, `i` is n, `mask` is less than 1 << n.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:The function `func` reads an input matrix `a` with dimensions N x N, where N is a positive integer, and each value in the matrix is either 0 or 1. The function then performs a specific operation on the input matrix `a`, calculating values in a 2D list `dp` based on bitwise operations. Finally, it prints the result stored at `dp[n][(1 << n) - 1]`. The exact details of the operation on the matrix are not explicitly mentioned in the annotations.


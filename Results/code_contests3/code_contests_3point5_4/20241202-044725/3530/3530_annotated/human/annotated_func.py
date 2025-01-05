#State of the program right berfore the function call: **Precondition**: **N is an integer such that 1 <= N <= 21. The compatibility matrix a is a 2D list of integers where a_{i,j} is either 0 or 1.**
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: Output State: MOD is 1000000007, `n` is greater than 0, `a` is a list containing the result of mapping all input values to integers.
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: `MOD` is 1000000007, `n` is greater than 0, `a` is a list containing the result of mapping all input values to integers, `dp` is a 2D list of size (1 << n) x 1 initialized with ones
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: After all iterations of the loop have finished, `dp` contains the final updated values for each `i` and `mask` combination with the modulo operation using `MOD` as 1000000007. All other variables maintain their initial conditions - `MOD` remains 1000000007, `n` is still greater than 0, `j` is within the range 0 to `n-1`, and `mask` is within the range 1 to 2^n - 1.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:Functionality: The function `func` initializes a variable MOD with the value 1000000007. It then takes an input `n` and a 2D list `a` based on the input values. The function calculates and updates a 2D list `dp` using nested loops according to predefined conditions. After the loops, it prints a specific value from the `dp` list. The function processes the compatibility matrix `a` to calculate specific values in the `dp` list based on given conditions.


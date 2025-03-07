#State of the program right berfore the function call: n is a positive integer representing the size of the hidden array a, and p is a list of integers of length n representing the sorted prefix sums of array a, where each element in p satisfies |p_i| <= n.
def func_1(n, p):
    dp = [0] * (2 * n + 1)
    offset = n
    dp[offset] = 1
    for i in range(1, n + 1):
        new_dp = [0] * (2 * n + 1)
        
        for j in range(2 * n + 1):
            if dp[j] > 0:
                if j + 1 <= 2 * n:
                    new_dp[j + 1] = (new_dp[j + 1] + dp[j]) % MOD
                if j - 1 >= 0:
                    new_dp[j - 1] = (new_dp[j - 1] + dp[j]) % MOD
        
        dp = new_dp
        
    #State: `dp` is a list of `2 * n + 1` elements where `dp[j]` is the binomial coefficient `C(n, (n + j) / 2) % MOD` if `(n + j)` is even, and `0` if `(n + j)` is odd. All other variables remain unchanged.
    final_sum = p[-1] + offset
    return dp[final_sum]
    #The program returns `dp[dp[-1] + offset]`
#Overall this is what the function does:The function `func_1` takes a positive integer `n` and a list of integers `p` of length `n` as input. It computes and returns a specific value from a dynamic programming array `dp` based on the input parameters. The returned value is `dp[dp[-1] + offset]`, where `offset` is a predefined value within the function.

#State of the program right berfore the function call: n is a positive integer representing the size of the hidden array a, and p is a list of n integers representing the sorted prefix sums of array a.
def func_2():
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        
        index += 1
        
        p = list(map(int, data[index:index + n]))
        
        index += n
        
        result = func_1(n, p)
        
        results.append(result)
        
    #State: `n` is the integer value from the last iteration, `p` is the list of integers from the last iteration, `index` is the position after the last `p` was read, `t` is the initial integer value, `data` is the initial list of strings, `input` is reassigned to `sys.stdin.read`, and `results` is a list of results from `func_1(n, p)` for each iteration.
    for res in results:
        print(res)
        
    #State: `n` is the integer value from the last iteration, `p` is the list of integers from the last iteration, `index` is the position after the last `p` was read, `t` is the initial integer value, `data` is the initial list of strings, `input` is reassigned to `sys.stdin.read`, and `results` is a list of results from `func_1(n, p)` for each iteration. The elements of `results` have been printed.
#Overall this is what the function does:The function reads input from standard input, processes multiple test cases, and for each test case, it reconstructs an array `a` from given prefix sums `p`. It then prints the reconstructed array for each test case.


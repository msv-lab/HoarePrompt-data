#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 5000), and p is a list of n integers sorted in non-decreasing order such that |p[i]| ≤ n for all 0 ≤ i < n.
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
        
    #State: `dp` is a list of 2n + 1 integers where the values are the result of the loop's operations, and all other variables (`n`, `p`, `offset`) remain unchanged.
    final_sum = p[-1] + offset
    return dp[final_sum]
    #The program returns the value of `dp[final_sum]`, where `final_sum` is equal to the last element of list `p` plus `offset`.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and a list `p` of `n` integers sorted in non-decreasing order. It returns an integer value from a dynamically computed list `dp`, where the index of the returned value is the last element of `p` plus an offset of `n`. The function does not modify the input parameters `n` or `p`.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n is an integer such that 1 <= n <= 5000, and p is a list of n integers where |p_i| <= n and p_1 <= p_2 <= ... <= p_n.
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
        
    #State: Output State: `t` is the integer value of `data[0]`, `n` is the integer value of the last `n` processed in the loop, `p` is the list of integers corresponding to the last `p` processed in the loop, `data` remains the same list of strings, `index` is the index after all the data has been processed, `results` is a list containing the results of `func_1(n, p)` for each iteration of the loop.
    for res in results:
        print(res)
        
    #State: The values of `t`, `n`, `p`, `data`, and `index` remain unchanged. `results` is a list containing the results of `func_1(n, p)` for each iteration of the loop, and each element of `results` is printed to the console.
#Overall this is what the function does:The function reads input from `sys.stdin`, processes multiple test cases, and prints the results of each test case to the console. Each test case consists of an integer `n` and a sorted list of `n` integers `p`. The function calls `func_1(n, p)` for each test case and appends the result to a list `results`. After processing all test cases, it prints each element of `results` to the console. The function does not return any value.


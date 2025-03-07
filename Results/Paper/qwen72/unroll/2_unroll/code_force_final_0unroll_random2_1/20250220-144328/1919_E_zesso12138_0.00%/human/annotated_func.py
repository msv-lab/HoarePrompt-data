#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 5000), and p is a list of n integers (|p_i| ≤ n) sorted in non-decreasing order.
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
        
    #State: `dp` is a list of 2n + 1 integers, all initialized to 0 except `dp[n - i]` and `dp[n + i]` which are 1 for each `i` from 1 to `n`, and `dp[n]` which is 0.
    final_sum = p[-1] + offset
    return dp[final_sum]
    #The program returns 1.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and a list `p` of `n` integers sorted in non-decreasing order. It initializes a list `dp` of size `2n + 1` with all elements set to 0, except for `dp[n]` which is set to 1. The function then updates the `dp` list based on the values of `p` and returns the value at the index `p[-1] + n` in the `dp` list. The final state of the program is that the function returns 1.

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
        
    #State: `t` is an integer such that 1 <= t <= 1000, `n` is the integer value of the last element in `data` that was used to define `n` in the loop, `p` is the list of integers from the last iteration of the loop, `data` is a list of strings obtained by splitting the input read from standard input until EOF, `index` is the integer value of the initial `index` plus the total number of elements processed in the loop (i.e., `t * (n + 1)` where `n` is the average number of elements in each `p` list), `results` is a list of `t` elements, each element being the result of `func_1(n, p)` for each iteration of the loop.
    for res in results:
        print(res)
        
    #State: The `results` list contains `t` elements, each being the result of `func_1(n, p)` from each iteration of the loop. The `index` is the initial `index` plus the total number of elements processed in the loop, which is `t * (n + 1)` where `n` is the average number of elements in each `p` list. The values of `t`, `n`, and `p` remain unchanged after the loop execution. The `data` list remains unchanged.
#Overall this is what the function does:The function reads a series of inputs from standard input. It processes `t` test cases, where `t` is an integer between 1 and 1000. For each test case, it reads an integer `n` (1 <= n <= 5000) and a sorted list `p` of `n` integers (each between -n and n). It then calls `func_1(n, p)` for each test case and appends the result to a list `results`. After processing all test cases, it prints each element in `results`. The function does not return any value, but it modifies the state of the program by reading from standard input and printing the results to the standard output.


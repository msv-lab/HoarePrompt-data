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
        
    #State: dp is a list of zeros of length `2 * n + 1`.
    final_sum = p[-1] + offset
    return dp[final_sum]
    #The program returns 0
#Overall this is what the function does:The function accepts two parameters: `n`, a positive integer representing the size of a hidden array `a`, and `p`, a list of integers of length `n` representing the sorted prefix sums of array `a`, where each element in `p` satisfies |p_i| <= n. Regardless of the input values, the function always returns 0.

#State of the program right berfore the function call: n is a positive integer representing the size of the hidden array a, and p is a list of integers of length n representing the sorted prefix sums of array a.
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
        
    #State: `t` is the integer value of `data[0]`; `index` is `1 + sum(1 + n_i for i in range(1, t+1))`; `results` is a list containing `t` elements, each the result of `func_1(n, p)` for the respective `n` and `p` in each iteration; `n` and `p` are the values used in the last iteration.
    for res in results:
        print(res)
        
    #State: `t` is 1, `index` is `1 + sum(1 + n_i for i in range(1, t+1))`, `results` is a list containing 1 element, which is the result of `func_1(n, p)` for the respective `n` and `p` in the iteration, `n` and `p` are the values used in the last iteration
#Overall this is what the function does:The function `func_2` reads multiple test cases from standard input. Each test case consists of an integer `n` and a list `p` of `n` integers representing the sorted prefix sums of an unknown array `a`. For each test case, it computes and prints the hidden array `a`.


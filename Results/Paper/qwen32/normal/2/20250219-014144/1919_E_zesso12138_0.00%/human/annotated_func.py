#State of the program right berfore the function call: n is a positive integer representing the size of the hidden array a, and p is a list of n integers representing the sorted prefix sums of array a such that |p_i| <= n for all i, and p is sorted in non-decreasing order.
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
        
    #State: `n` is a positive integer, `i` is `n + 1` (indicating the loop has completed), `p` is a list of `n` integers representing the sorted prefix sums of array `a` such that `|p_i| <= n` for all `i`, and `p` is sorted in non-decreasing order; `dp` is a list of `2 * n + 1` integers with non-zero values spread out from the initial position `dp[n]` after `n` iterations; `offset` is `n`; `new_dp` is a list of `2 * n + 1` integers, all initialized to 0.
    final_sum = p[-1] + offset
    return dp[final_sum]
    #The program returns a non-zero value from `dp[final_sum]` where `final_sum` is `p[-1] + n`.
#Overall this is what the function does:The function `func_1` calculates and returns a specific value from a dynamic programming array `dp` based on the size `n` of a hidden array `a` and a list `p` of its sorted prefix sums. The returned value is located at the index `final_sum`, which is determined by adding the last element of `p` to `n`.

#State of the program right berfore the function call: n is a positive integer representing the size of the hidden array a, and p is a list of n integers representing the sorted prefix sums of array a, where |p_i| <= n for all i, and p is sorted in non-decreasing order.
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
        
    #State: `n` is the size of the last array `p` processed; `p` is the last array of integers derived from `data`; `data` is a list of strings; `index` is `1 + t + sum of sizes of all arrays p`; `t` is 0; `results` is a list containing `t` elements, each being the return value of `func_1(n, p)` for each iteration; `result` holds the return value of `func_1(n, p)` from the last iteration.
    for res in results:
        print(res)
        
    #State: The loop has printed all elements in `results`. `n` is the size of the last array `p` processed, `p` is the last array of integers derived from `data`, `data` is a list of strings, `index` is `1 + t + sum of sizes of all arrays p`, `t` is 0, `results` is a list containing the return values of `func_1(n, p)` for each iteration, `result` holds the return value of `func_1(n, p)` from the last iteration.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer `n` and a list `p` of `n` integers representing the sorted prefix sums of an unknown array `a`. For each test case, it computes and prints the hidden array `a`.


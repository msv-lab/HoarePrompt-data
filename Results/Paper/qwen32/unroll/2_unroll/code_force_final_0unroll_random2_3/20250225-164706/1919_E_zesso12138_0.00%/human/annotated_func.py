#State of the program right berfore the function call: n is a positive integer representing the size of the hidden array a, and p is a list of n integers representing the sorted prefix sums of a, where each element in p satisfies |p_i| <= n.
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
        
    #State: dp is a list of 2 * n + 1 integers where dp[n-i] and dp[n+i] for i from 0 to n are non-zero, and all other elements are 0.
    final_sum = p[-1] + offset
    return dp[final_sum]
    #The program returns the value at index `final_sum` in the `dp` list, which is non-zero if `final_sum` is within the range `[n-i, n+i]` for some `i`, otherwise, it is 0.
#Overall this is what the function does:The function `func_1` takes two parameters: `n`, a positive integer representing the size of a hidden array, and `p`, a list of `n` integers representing the sorted prefix sums of the array. The function returns a value from the `dp` list at an index determined by `final_sum`. This value is non-zero if `final_sum` falls within the range `[n-i, n+i]` for some `i`; otherwise, it returns 0.

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
        
    #State: `n` is the size of the last processed array `p`; `p` is the last processed list of integers; `input` holds the entire input provided as a string; `data` is a list of strings obtained by splitting `input` on whitespace; `index` is the position in `data` after processing all `t` arrays; `t` is the integer value of `data[0]`; `results` is a list of `t` elements, each being the result of `func_1` for the corresponding `n` and `p`.
    for res in results:
        print(res)
        
    #State: n is the size of the last processed array p; p is the last processed list of integers; input holds the entire input provided as a string; data is a list of strings obtained by splitting input on whitespace; index is the position in data after processing all t arrays; t is the integer value of data[0]; results is a list of t elements, each being the result of func_1 for the corresponding n and p. The contents of results have been printed.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer `n` and a list `p` of `n` integers representing sorted prefix sums. For each test case, it computes and prints the hidden array `a` that corresponds to these prefix sums.


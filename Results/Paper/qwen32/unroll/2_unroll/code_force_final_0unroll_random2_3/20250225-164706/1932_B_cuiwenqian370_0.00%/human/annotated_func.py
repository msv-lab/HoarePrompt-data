#State of the program right berfore the function call: path is a list (or string) of characters.
def func_1(path):
    n = len(path)
    if (n == 0) :
        return 0
        #The program returns 0
    #State: `path` is a list (or string) of characters; `n` is the length of `path`, and `n` is greater than 0.
    dp = [0] * n
    if (path[0] == '@') :
        dp[0] = 1
    else :
        if (path[0] == '*') :
            dp[0] = -float('inf')
        #State: `path` is a list (or string) of characters, `n` is the length of `path`, and `n` is greater than 0. If the first character of `path` is `*`, then `dp` is a list where the first element is `-float('inf')` and the rest are zeros. Otherwise, `dp` remains a list of zeros. The first character of `path` is not `@`.
    #State: `path` is a list (or string) of characters, and `n` is the length of `path`, with `n` greater than 0. If the first character of `path` is `@`, then `dp` is a list of zeros with length `n`, except `dp[0]` is 1. If the first character of `path` is `*`, then `dp` is a list where the first element is `-float('inf')` and the rest are zeros. If the first character of `path` is neither `@` nor `*`, then `dp` remains a list of zeros.
    if (n > 1) :
        if (path[1] == '*') :
            dp[1] = -float('inf')
        else :
            dp[1] = dp[0] + (1 if path[1] == '@' else 0)
        #State: `path` is a list (or string) of characters, and `n` is the length of `path`, with `n` greater than 1. If the first character of `path` is `@`, then `dp` is a list of zeros with length `n`, except `dp[0]` is 1. If the second character of `path` is `*`, `dp[1]` is `-float('inf')`; otherwise, `dp[1]` is 1 if the second character of `path` is `@`, otherwise `dp[1]` is 0. If the first character of `path` is `*`, then `dp` is a list where the first element is `-float('inf')` and the rest are zeros. If the second character of `path` is `*`, `dp[1]` is `-float('inf')`; otherwise, `dp[1]` is 0 if the second character of `path` is `@`, otherwise `dp[1]` is 0. If the first character of `path` is neither `@` nor `*`, then `dp` remains a list of zeros, except `dp[1]` is 1 if the second character of `path` is `@`, otherwise `dp[1]` is 0.
    #State: `path` is a list (or string) of characters, and `n` is the length of `path`, with `n` greater than 0. If the first character of `path` is `@`, then `dp` is a list of zeros with length `n`, except `dp[0]` is 1. If `n` is greater than 1, `dp[1]` is `-float('inf')` if the second character of `path` is `*`, otherwise `dp[1]` is 1 if the second character of `path` is `@`, otherwise `dp[1]` is 0. If the first character of `path` is `*`, then `dp` is a list where the first element is `-float('inf')` and the rest are zeros. If `n` is greater than 1, `dp[1]` is `-float('inf')` if the second character of `path` is `*`, otherwise `dp[1]` is 0 if the second character of `path` is `@`, otherwise `dp[1]` is 0. If the first character of `path` is neither `@` nor `*`, then `dp` remains a list of zeros, except `dp[1]` is 1 if the second character of `path` is `@`, otherwise `dp[1]` is 0.
    for i in range(2, n):
        if path[i] == '*':
            dp[i] = -float('inf')
        else:
            dp[i] = max(dp[i - 1], dp[i - 2]) + (1 if path[i] == '@' else 0)
        
    #State: [1, -inf, 2, 3, -inf]
    return max(x for x in dp if x > -float('inf'))
    #The program returns 3
#Overall this is what the function does:The function evaluates a path consisting of characters and returns the maximum count of '@' characters that can be encountered without encountering a '*'. If the path is empty, it returns 0.

#State of the program right berfore the function call: path is a string of space-separated integers representing the periodicities of the signs, and n is an integer representing the number of signs such that 1 <= n <= 100.
def func_2():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        
        index += 1
        
        path = data[index]
        
        index += 1
        
        results.append(func_1(path))
        
    #State: `path` is the last path string processed, `n` is the last integer representing the number of signs processed, `data` remains the same, `t` remains the same, `index` is `1 + 2 * t`, `results` is a list of results from `func_1(path)` for each iteration.
    for result in results:
        print(result)
        
    #State: path is the last path string processed, n is the last integer representing the number of signs processed, data remains the same, t remains the same, index is 1 + 2 * t, results is a list of results from func_1(path) for each iteration.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer `n` and a string `path`. It processes each test case using the `func_1` function and prints the result for each case.


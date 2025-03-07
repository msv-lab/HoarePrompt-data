#State of the program right berfore the function call: **t is an integer such that 1 ≤ t ≤ 100, n is an integer such that 1 ≤ n ≤ 100, and a_i is an integer such that 1 ≤ a_i ≤ 10^6 for all 1 ≤ i ≤ n.
def func_1(path):
    n = len(path)
    if (n == 0) :
        return 0
        #The program returns 0
    #State: Postcondition: `t` is an integer such that 1 ≤ t ≤ 100, `n` is greater than 0, and `a_i` is an integer such that 1 ≤ a_i ≤ 10^6 for all 1 ≤ i ≤ n.
    dp = [0] * n
    if (path[0] == '@') :
        dp[0] = 1
    else :
        if (path[0] == '*') :
            dp[0] = -float('inf')
        #State: `dp` is a list of length `n` where the first element is `-inf` and all other elements are 0, `t` is an integer such that 1 ≤ t ≤ 100, `n` is greater than 0, and `a_i` is an integer such that 1 ≤ a_i ≤ 10^6 for all 1 ≤ i ≤ n, and `path[0]` is '*', `path[0]` is not '@'.
    #State: Postcondition: `dp` is a list of length `n` where either the first element is 1 and all other elements are 0, or the first element is `-inf` and all other elements are 0. `t` is an integer such that 1 ≤ t ≤ 100, `n` is greater than 0, and `a_i` is an integer such that 1 ≤ a_i ≤ 10^6 for all 1 ≤ i ≤ n. Additionally, `path[0]` is either '@' or '*'.
    if (n > 1) :
        if (path[1] == '*') :
            dp[1] = -float('inf')
        else :
            dp[1] = dp[0] + (1 if path[1] == '@' else 0)
        #State: Postcondition: `dp` is a list of length `n` where either the first element is 1 and all other elements are 0, or the first element is `-inf` and all other elements are 0; `dp[1]` is either `dp[0] + 1` if `path[1] == '@'` or `dp[0]` if `path[1] == '*'`; `t` is an integer such that 1 ≤ t ≤ 100; `n` is greater than 1; `a_i` is an integer such that 1 ≤ a_i ≤ 10^6 for all 1 ≤ i ≤ n; `path[0]` is either '@' or '*'.
    #State: Postcondition: `dp` is a list of length `n` where either the first element is 1 and all other elements are 0, or the first element is `-inf` and all other elements are 0; `dp[1]` is either `dp[0] + 1` if `path[1] == '@'` or `dp[0]` if `path[1] == '*'`; `t` is an integer such that 1 ≤ t ≤ 100; `n` is greater than 1; `a_i` is an integer such that 1 ≤ a_i ≤ 10^6 for all 1 ≤ i ≤ n; `path[0]` is either '@' or '*'.
    for i in range(2, n):
        if path[i] == '*':
            dp[i] = -float('inf')
        else:
            dp[i] = max(dp[i - 1], dp[i - 2]) + (1 if path[i] == '@' else 0)
        
    #State: dp is a list of length n where each dp[i] (for 0 ≤ i < n) is calculated based on the previous elements in dp and the characters in path. Specifically, dp[0] is 1 or -inf depending on path[0], dp[1] is dp[0] + 1 if path[1] == '@' or dp[0] if path[1] == '*', and for each i from 2 to n-1, dp[i] is the maximum of dp[i-1] and dp[i-2] plus 1 if path[i] == '@', otherwise it's just the maximum of dp[i-1] and dp[i-2]. t remains an integer such that 1 ≤ t ≤ 100, and n is greater than 1 with each a_i being an integer such that 1 ≤ a_i ≤ 10^6.
    return max(x for x in dp if x > -float('inf'))
    #The program returns the maximum value in the list `dp` that is greater than negative infinity.
#Overall this is what the function does:The function `func_1` accepts a parameter `path`, which is a list of characters. It initializes a dynamic programming list `dp` to keep track of certain values based on the characters in `path`. Depending on the first character of `path`, `dp[0]` is set to either 1 or `-inf`. For subsequent characters, `dp[i]` is calculated as the maximum of `dp[i-1]` and `dp[i-2]` plus 1 if the current character is '@', or just the maximum of `dp[i-1]` and `dp[i-2]` if the current character is '*'. Finally, the function returns 0 if no valid value in `dp` is greater than `-inf`, otherwise it returns the maximum value in `dp` that is greater than `-inf`.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 100, representing the number of signs. The next line contains n space-separated integers a_1, a_2, a_3, ..., a_n such that 1 ≤ a_i ≤ 10^6, representing the periodicities of the signs.
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
        
    #State: Output State: `t` is the number of iterations in the loop, `data` is a list of strings obtained by splitting the input string on whitespace, `index` is `t + 2`, `results` is a list containing `t` elements, each element being the result of calling `func_1` with a path string from the `data` list.
    for result in results:
        print(result)
        
    #State: Output State: `t` is the number of iterations in the loop, `data` is a list of strings obtained by splitting the input string on whitespace, `index` is `t + 2`, `results` is a list containing `t` elements, each element being the result of calling `func_1` with a path string from the `data` list, the loop has executed all iterations, and the output consists of printing each element in the `results` list.
#Overall this is what the function does:The function processes a series of test cases, each containing an integer `t` indicating the number of test cases, followed by `t` groups of data. Each group includes an integer `n` indicating the number of signs, and `n` space-separated integers representing the periodicities of the signs. For each group, it calls `func_1` with a path string and collects the results. Finally, it prints each result from the collected list.


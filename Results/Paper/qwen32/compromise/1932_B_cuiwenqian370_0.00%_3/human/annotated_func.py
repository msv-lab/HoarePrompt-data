#State of the program right berfore the function call: path is a list of characters, where each character can be either '@' or '*'.
def func_1(path):
    n = len(path)
    if (n == 0) :
        return 0
        #The program returns 0
    #State: `path` is a list of characters, where each character can be either '@' or '*'; `n` is the length of `path` and `n` is greater than 0
    dp = [0] * n
    if (path[0] == '@') :
        dp[0] = 1
    else :
        if (path[0] == '*') :
            dp[0] = -float('inf')
        #State: `path` is a list of characters, where each character can be either '@' or '*'; `n` is the length of `path` and `n` is greater than 0. If the first element of `path` is '*', then the first element of `dp` is set to `-float('inf')`. Otherwise, `dp` remains a list of `n` zeros. The first element of `path` is '*'.
    #State: `path` is a list of characters where each character can be either '@' or '*', `n` is the length of `path` and `n` is greater than 0. If the first element of `path` is '@', then the first element of `dp` is `1`. Otherwise, the first element of `dp` is `-float('inf')`. The rest of `dp` remains a list of zeros.
    if (n > 1) :
        if (path[1] == '*') :
            dp[1] = -float('inf')
        else :
            dp[1] = dp[0] + (1 if path[1] == '@' else 0)
        #State: `path` is a list of characters where each character can be either '@' or '*', and `n` is the length of `path` with `n` greater than 1. If the first element of `path` is '@', then the first element of `dp` is `1`; otherwise, the first element of `dp` is `-float('inf')`. The second element of `dp` is `-float('inf')` if the second element of `path` is '*', otherwise it is `dp[0] + 1` if the second element of `path` is '@', or `dp[0]` if the second element of `path` is not '@'. The rest of `dp` remains a list of zeros.
    #State: `path` is a list of characters where each character can be either '@' or '*', and `n` is the length of `path` with `n` greater than 0. If `n` is 1, `dp` remains a list where the first element is `1` if the first element of `path` is '@', otherwise it is `-float('inf')`, and the rest of `dp` is zeros. If `n` is greater than 1, the first element of `dp` is `1` if the first element of `path` is '@', otherwise it is `-float('inf')`. The second element of `dp` is `-float('inf')` if the second element of `path` is '*', otherwise it is `dp[0] + 1` if the second element of `path` is '@', or `dp[0]` if the second element of `path` is not '@'. The rest of `dp` remains zeros.
    for i in range(2, n):
        if path[i] == '*':
            dp[i] = -float('inf')
        else:
            dp[i] = max(dp[i - 1], dp[i - 2]) + (1 if path[i] == '@' else 0)
        
    #State: dp = [1, -float('inf'), 2, 3]
    return max(x for x in dp if x > -float('inf'))
    #The program returns 3.
#Overall this is what the function does:The function `func_1` accepts a parameter `path`, which is a list of characters where each character can be either '@' or '*'. It calculates the maximum number of '@' characters that can be collected by traversing the list from left to right, with the condition that encountering a '*' character resets the count to negative infinity, effectively disqualifying any sequence containing '*'. The function returns the maximum count of '@' characters found in any valid subsequence of `path`. If `path` is empty, it returns 0.

#State of the program right berfore the function call: path is a string representing a sequence of space-separated integers, n is an integer such that 1 <= n <= 100, and the integers in path represent the periodicities of the signs, each being between 1 and 10^6 inclusive.
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
        
    #State: `path` is the string at `data[2 * t]`, `n` is the integer value of the string at `data[2 * t - 1]`, `data` remains unchanged, `t` remains unchanged, `index` is `2 * t + 1`, and `results` contains the results of `func_1(path)` for each iteration.
    #
    #Output State:
    for result in results:
        print(result)
        
    #State: path is the string at data[2 * t], n is the integer value of the string at data[2 * t - 1], data remains unchanged, t remains unchanged, index is 2 * t + 1, and results contains the results of func_1(path) for each iteration. The loop has printed each result in results to the console.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer `n` and a string `path`. It processes each test case using the `func_1` function and prints the result for each test case.


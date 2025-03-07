#State of the program right berfore the function call: path is a non-empty list of strings where each string is either '@', '*', or some other character.
def func_1(path):
    n = len(path)
    if (n == 0) :
        return 0
        #The program returns 0.
    #State: `path` is a non-empty list of strings where each string is either '@', '*', or some other character, `n` is the length of `path`, and `n` is greater than 0.
    dp = [0] * n
    if (path[0] == '@') :
        dp[0] = 1
    else :
        if (path[0] == '*') :
            dp[0] = -float('inf')
        #State: *`path` is a non-empty list of strings where each string is either '*', or some other character (but not '@'), `n` is the length of `path`, and `n` is greater than 0; `dp` is a list of length `n` with all elements initialized to 0. If the first element of `path` is '*', then the first element of `dp` is set to `-inf`.
    #State: *`path` is a non-empty list of strings where each string is either '@', '*', or some other character, `n` is the length of `path`, and `n` is greater than 0; `dp` is a list of length `n` with all elements initialized to 0. If the first element of `path` is '@', then `dp[0]` is set to 1. If the first element of `path` is '*', then `dp[0]` is set to `-inf`. If the first element of `path` is neither '@' nor '*', then `dp[0]` remains 0.
    if (n > 1) :
        if (path[1] == '*') :
            dp[1] = -float('inf')
        else :
            dp[1] = dp[0] + (1 if path[1] == '@' else 0)
        #State: `path` is a non-empty list of strings where each string is either '@', '*', or some other character, `n` is the length of `path`, and `n` is greater than 1; `dp` is a list of length `n` with all elements initialized to 0. If the first element of `path` is '@', then `dp[0]` is set to 1. If the first element of `path` is '*', then `dp[0]` is set to `-inf`. If the first element of `path` is neither '@' nor '*', then `dp[0]` remains 0. If the second element of `path` is '*', then `dp[1]` is set to `-inf`. If the second element of `path` is not '*', then `dp[1]` is set to 1 if `path[1]` is '@' or 0 otherwise.
    #State: *`path` is a non-empty list of strings where each string is either '@', '*', or some other character, `n` is the length of `path`, and `n` is greater than 0; `dp` is a list of length `n` with all elements initialized to 0. If the first element of `path` is '@', then `dp[0]` is set to 1. If the first element of `path` is '*', then `dp[0]` is set to `-inf`. If the first element of `path` is neither '@' nor '*', then `dp[0]` remains 0. If `n` > 1, and the second element of `path` is '*', then `dp[1]` is set to `-inf`. If the second element of `path` is not '*', then `dp[1]` is set to 1 if `path[1]` is '@' or 0 otherwise. If `n` is 1, `dp` remains unchanged except for `dp[0]` as described above.
    for i in range(2, n):
        if path[i] == '*':
            dp[i] = -float('inf')
        else:
            dp[i] = max(dp[i - 1], dp[i - 2]) + (1 if path[i] == '@' else 0)
        
    #State: `path` remains a non-empty list of strings where each string is either '@', '*', or some other character, `n` is the length of `path`, and `n` is greater than 0; `dp` is a list of length `n` where `dp[i]` is set to `-inf` if `path[i]` is '*', otherwise `dp[i]` is set to the maximum of `dp[i-1]` and `dp[i-2]` plus 1 if `path[i]` is '@' or 0 otherwise.
    return max(x for x in dp if x > -float('inf'))
    #The program returns the maximum value in the `dp` list that is greater than negative infinity. This value is calculated based on the conditions: if `path[i]` is '*', `dp[i]` is set to `-inf`; if `path[i]` is '@', `dp[i]` is set to the maximum of `dp[i-1]` and `dp[i-2]` plus 1; otherwise, `dp[i]` is set to the maximum of `dp[i-1] and `dp[i-2]` plus 0.
#Overall this is what the function does:The function `func_1` accepts a parameter `path`, which is a non-empty list of strings. Each string in `path` is either '@', '*', or some other character. The function returns the maximum value in a derived list `dp` that is greater than negative infinity. The `dp` list is constructed such that for each index `i` in `path`:
- If `path[i]` is '*', `dp[i]` is set to `-inf`.
- If `path[i]` is '@', `dp[i]` is set to the maximum of `dp[i-1]` and `dp[i-2]` plus 1.
- If `path[i]` is neither '@' nor '*', `dp[i]` is set to the maximum of `dp[i-1]` and `dp[i-2]` plus 0.
If all elements in `path` are '*', the function returns 0.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and data is a list of strings containing the input data for t test cases.
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
        
    #State: Output State: `t` is an integer equal to the integer value of `data[0]`, `data` is a list of strings containing the input data for `t` test cases, `input` is now a function that reads from `sys.stdin`, `data` is updated to a list of strings split from the input read by `input()`, `index` is `1 + 2 * t`, `results` is a list containing the results of `func_1(path)` for each test case.
    for result in results:
        print(result)
        
    #State: The loop has printed each element in the `results` list, and the variables `t`, `data`, `input`, `index`, and `results` remain unchanged.
#Overall this is what the function does:The function reads from `sys.stdin`, processes `t` test cases where `t` is an integer such that `1 <= t <= 1000`, and each test case consists of an integer `n` and a string `path`. It applies `func_1` to each `path` and prints the results. After the function concludes, `t` is the integer value of `data[0]`, `data` is a list of strings split from the input, `index` is `1 + 2 * t`, and `results` is a list containing the results of `func_1(path)` for each test case. The function does not return any value.


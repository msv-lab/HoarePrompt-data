#State of the program right berfore the function call: path is a list of strings where each string is either '@', '*', or some other character representing the signs, and the length of path is at least 0.
def func_1(path):
    n = len(path)
    if (n == 0) :
        return 0
        #The program returns 0.
    #State: *`path` is a list of strings where each string is either '@', '*', or some other character representing the signs, and the length of `path` is at least 1; `n` is the length of `path` and is greater than 0
    dp = [0] * n
    if (path[0] == '@') :
        dp[0] = 1
    else :
        if (path[0] == '*') :
            dp[0] = -float('inf')
        #State: *`path` is a list of strings where each string is either '*', or some other character representing the signs, and the length of `path` is at least 1; `n` is the length of `path` and is greater than 0; `dp` is a list of zeros with length `n`. If the first element of `path` is '*', the first element of `dp` is set to `-inf`. The first element of `path` is not '@'.
    #State: *`path` is a list of strings where each string is either '@', '*', or some other character representing the signs, and the length of `path` is at least 1; `n` is the length of `path` and is greater than 0; `dp` is a list of zeros with length `n`. If the first element of `path` is '@', `dp[0]` is set to 1. If the first element of `path` is '*', `dp[0]` is set to `-inf`. If the first element of `path` is neither '@' nor '*', `dp[0]` remains 0.
    if (n > 1) :
        if (path[1] == '*') :
            dp[1] = -float('inf')
        else :
            dp[1] = dp[0] + (1 if path[1] == '@' else 0)
        #State: *`path` is a list of strings where each string is either '@', '*', or some other character, and the length of `path` is at least 1; `n` is the length of `path` and is greater than 1; `dp` is a list of zeros with length `n`. If the first element of `path` is '@', `dp[0]` is set to 1. If the first element of `path` is '*', `dp[0]` is set to `-inf`. If the first element of `path` is neither '@' nor '*', `dp[0]` remains 0. If the second element of `path` is '*', `dp[1]` is set to `-inf`. If the second element of `path` is not '*', `dp[1]` is updated based on the value of `dp[0]` and whether `path[1]` is '@': If `path[0]` is '@' and `path[1]` is '@', `dp[1]` is 2. If `path[0]` is '@' and `path[1]` is not '@', `dp[1]` is 1. If `path[0]` is '*' and `path[1]` is '@', `dp[1]` is `-inf`. If `path[0]` is '*' and `path[1]` is not '@', `dp[1]` is `-inf`. If `path[0]` is neither '@' nor '*' and `path[1]` is '@', `dp[1]` is 1. If `path[0]` is neither '@' nor '*' and `path[1]` is not '@', `dp[1]` is 0.
    #State: *`path` is a list of strings where each string is either '@', '*', or some other character, and the length of `path` is at least 1; `n` is the length of `path` and is greater than 0; `dp` is a list of zeros with length `n`. If the first element of `path` is '@', `dp[0]` is set to 1. If the first element of `path` is '*', `dp[0]` is set to `-inf`. If the first element of `path` is neither '@' nor '*', `dp[0]` remains 0. If `n` > 1, `dp[1]` is updated as follows: If the second element of `path` is '*', `dp[1]` is set to `-inf`. If the second element of `path` is not '*', `dp[1]` is updated based on the value of `dp[0]` and whether `path[1]` is '@': If `path[0]` is '@' and `path[1]` is '@', `dp[1]` is 2. If `path[0]` is '@' and `path[1]` is not '@', `dp[1]` is 1. If `path[0]` is '*' and `path[1]` is '@', `dp[1]` is `-inf`. If `path[0]` is '*' and `path[1]` is not '@', `dp[1]` is `-inf`. If `path[0]` is neither '@' nor '*' and `path[1]` is '@', `dp[1]` is 1. If `path[0]` is neither '@' nor '*' and `path[1]` is not '@', `dp[1]` is 0. If `n` is 1, `dp` remains unchanged.
    for i in range(2, n):
        if path[i] == '*':
            dp[i] = -float('inf')
        else:
            dp[i] = max(dp[i - 1], dp[i - 2]) + (1 if path[i] == '@' else 0)
        
    #State: `path` is a list of strings where each string is either '@', '*', or some other character, and the length of `path` is at least 1; `n` is the length of `path` and is greater than 0; `dp` is a list of integers with length `n`, where each element of `dp` has been updated according to the rules specified in the loop. The final value of `i` is `n`.
    return max(x for x in dp if x > -float('inf'))
    #The program returns the maximum value from the list `dp` that is greater than negative infinity.
#Overall this is what the function does:The function `func_1` takes a list `path` of strings, where each string is either '@', '*', or another character. It returns the maximum number of consecutive '@' characters that can be collected without encountering a '*' character. If the list is empty, the function returns 0. If no valid path (without encountering '*') exists, the function also returns 0.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases, where 1 ≤ t ≤ 1000. n is a positive integer representing the number of signs, where 1 ≤ n ≤ 100. path is a string containing n space-separated integers a_1, a_2, ..., a_n, where 1 ≤ a_i ≤ 10^6, representing the periodicities of the signs.
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
        
    #State: `t` is 0, `n` is the integer value of `data[index - 2]`, `index` is `2 * t + 1` (where `t` is the initial value of `t`), `path` is `data[index - 1]`, `results` contains the results of `func_1(path)` for each iteration of the loop.
    for result in results:
        print(result)
        
    #State: `t` is 0, `n` is the integer value of `data[index - 2]`, `index` is 1, `path` is `data[0]`, `results` must be a list with all elements processed, and `result` is the last element in `results`.
#Overall this is what the function does:The function reads input from standard input, processes multiple test cases, and prints the results. Each test case involves reading a number of signs and their periodicities, then applying a function (`func_1`) to these periodicities. The function does not return any value; instead, it prints the results of `func_1` for each test case. After the function completes, the input data has been fully processed, and the results have been printed to the standard output.


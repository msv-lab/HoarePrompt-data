#State of the program right berfore the function call: path is a string consisting of '@' and '*' characters, where the length of the string is at least 1.
def func_1(path):
    n = len(path)
    if (n == 0) :
        return 0
        #The program returns 0
    #State: `path` is a string consisting of '@' and '*' characters, `n` is the length of `path`, and `n` is not equal to 0
    dp = [0] * n
    if (path[0] == '@') :
        dp[0] = 1
    else :
        if (path[0] == '*') :
            dp[0] = -float('inf')
        #State: Postcondition: `path` is a string consisting of '@' and '*' characters, `n` is the length of `path`, `dp` is a list of `n` zeros. If the first character of `path` is '*', then the first element of `dp` is set to -inf. Otherwise, the first element of `dp` remains 0.
    #State: Postcondition: `path` is a string consisting of '@' and '*' characters, `n` is the length of `path`, and `dp` is a list of `n` zeros. If the first character of `path` is '@', then the first element of `dp` is set to 1. If the first character of `path` is '*', then the first element of `dp` is set to -inf. Otherwise, the first element of `dp` remains 0.
    if (n > 1) :
        if (path[1] == '*') :
            dp[1] = -float('inf')
        else :
            dp[1] = dp[0] + (1 if path[1] == '@' else 0)
        #State: Postcondition: `path` is a string consisting of '@' and '*' characters, `n` is the length of `path`, and `dp` is a list of `n` elements. The first element of `dp` is 1 if the first character of `path` is '@', -inf if the first character of `path` is '*', or 0 otherwise. The second element of `dp` is -inf if the second character of `path` is '*', 1 if the second character of `path` is '@', or `dp[0] + (1 if path[1] == '@' else 0)` if the second character is neither '@' nor '*'.
    #State: Postcondition: `path` is a string consisting of '@' and '*' characters, `n` is the length of `path`, and `dp` is a list of `n` elements. The first element of `dp` is 1 if the first character of `path` is '@', -inf if the first character of `path` is '*', or 0 otherwise. For each subsequent element `dp[i]` (where `i > 0`), it is -inf if the `(i+1)`-th character of `path` is '*', 1 if the `(i+1)`-th character of `path` is '@', or `dp[i-1] + (1 if path[i] == '@' else 0)` if the `(i+1)`-th character is neither '@' nor '*'.
    for i in range(2, n):
        if path[i] == '*':
            dp[i] = -float('inf')
        else:
            dp[i] = max(dp[i - 1], dp[i - 2]) + (1 if path[i] == '@' else 0)
        
    #State: dp is a list where each element dp[i] (for i > 1) is calculated based on the characters in the string 'path'. If the (i+1)-th character is '*', dp[i] is set to -inf. If the (i+1)-th character is '@', dp[i] is set to 1. Otherwise, dp[i] is the maximum of dp[i-1] and dp[i-2] plus 1 if the (i+1)-th character is '@', or 0 otherwise. The first element of dp is 1 if the first character of path is '@', -inf if the first character of path is '*', or 0 otherwise.
    return max(x for x in dp if x > -float('inf'))
    #The program returns the maximum value in the list `dp` that is greater than negative infinity.
#Overall this is what the function does:The function accepts a string `path` consisting of '@' and '*' characters and returns either 0 or the maximum value in the list `dp` that is greater than negative infinity. If the string `path` is empty, it returns 0. Otherwise, it calculates a dynamic programming list `dp` where each element depends on the characters in `path`. The final result is the maximum valid value in `dp`.

#State of the program right berfore the function call: t is an integer representing the number of test cases, n is an integer representing the number of signs for each test case, and path is a string containing n space-separated integers representing the periodicities of the signs for each test case.
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
        
    #State: Output State: `data` is a list of strings obtained by splitting the input string using spaces, `t` is an integer equal to `int(data[0])`, `n` is an integer representing the number of signs for each test case, `index` is equal to `t + 2`, `results` is a list containing the outputs of `func_1(path)` for each test case.
    for result in results:
        print(result)
        
    #State: `data` is a list of strings obtained by splitting the input string using spaces, `t` is an integer equal to `int(data[0])`, `n` is an integer representing the number of signs for each test case, `index` is equal to `t + 2`, `results` is a list containing the outputs of `func_1(path)` for each test case, the loop has executed all iterations, and `result` contains the last printed value from `func_1(path)`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads the number of signs and their periodicities from the input, calls another function `func_1` to compute some result based on these periodicities, and stores the result. After processing all test cases, it prints the computed results for each test case.


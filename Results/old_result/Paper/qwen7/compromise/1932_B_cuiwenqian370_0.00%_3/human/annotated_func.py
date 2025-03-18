#State of the program right berfore the function call: path is a string consisting of '@' and '*' characters, where the length of the string is at least 1.
def func_1(path):
    n = len(path)
    if (n == 0) :
        return 0
        #The program returns 0
    #State: `path` is a string consisting of '@' and '*' characters, and the length of `path` is not 0
    dp = [0] * n
    if (path[0] == '@') :
        dp[0] = 1
    else :
        if (path[0] == '*') :
            dp[0] = -float('inf')
        #State: Postcondition: `path` is a string consisting of '@' and '*' characters, and the length of `path` is not 0; `dp` is a list of length equal to the length of `path`, with all elements initialized to 0; if the first character of `path` is '*', then `dp[0]` is set to -inf.
    #State: Postcondition: `path` is a string consisting of '@' and '*' characters, and the length of `path` is not 0; `dp` is a list of length equal to the length of `path`, with all elements initialized to 0. If the first character of `path` is '@', then `dp[0]` is set to 1. Otherwise, if the first character of `path` is '*', then `dp[0]` is set to -inf.
    if (n > 1) :
        if (path[1] == '*') :
            dp[1] = -float('inf')
        else :
            dp[1] = dp[0] + (1 if path[1] == '@' else 0)
        #State: `path` is a string consisting of '@' and '*' characters, and the length of `path` is not 0; `dp` is a list of length equal to the length of `path`, with all elements initialized to 0; `dp[0]` is either 1 or -inf depending on the first character of `path`; `dp[1]` is -inf if the second character of `path` is '*', otherwise `dp[1] = dp[0] + (1 if path[1] == '@' else 0)`
    #State: Postcondition: `path` is a string consisting of '@' and '*' characters, and the length of `path` is not 0; `dp` is a list of length equal to the length of `path`, with all elements initialized to 0; `dp[0]` is either 1 or -inf depending on the first character of `path`; `dp[1]` is -inf if the second character of `path` is '*', otherwise `dp[1] = dp[0] + (1 if path[1] == '@' else 0)`.
    #
    #This postcondition summarizes the state of the variables `path` and `dp` after the execution of the if-else block. It covers both the if part and the absence of an else part, ensuring that all possible outcomes are accounted for based on the conditions and updates within the if statement.
    for i in range(2, n):
        if path[i] == '*':
            dp[i] = -float('inf')
        else:
            dp[i] = max(dp[i - 1], dp[i - 2]) + (1 if path[i] == '@' else 0)
        
    #State: Output State: `path` is a string consisting of '@' and '*' characters, and the length of `path` is `n`; `dp` is a list of length `n`, with `dp[0]` being either 1 or -inf depending on the first character of `path`, `dp[1]` being -inf if the second character of `path` is '*', otherwise `dp[1] = dp[0] + (1 if path[1] == '@' else 0)`, and for each `i` from 2 to `n-1`, `dp[i]` is -inf if `path[i]` is '*', otherwise `dp[i]` is the maximum of `dp[i-1]` and `dp[i-2]` plus 1 if `path[i]` is '@', 0 otherwise.
    return max(x for x in dp if x > -float('inf'))
    #The program returns the maximum value among the elements in the list `dp` that are greater than negative infinity.
#Overall this is what the function does:The function `func_1` accepts a string `path` consisting of '@' and '*' characters and returns either 0 or the maximum value among the elements in the list `dp` that are greater than negative infinity. If `path` is empty, the function returns 0. Otherwise, it constructs a dynamic programming array `dp` where each element depends on previous elements based on the characters in `path`. The function finally returns the highest valid value in `dp` that is not negative infinity.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 100, representing the number of signs. The next line contains n space-separated integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^6, representing the periodicities of the signs.
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
        
    #State: Output State: `t` is an integer, `data` is a list of strings, `index` is `2 * t`, `results` is a list containing `t` elements where each element is the result of `func_1(path)` for each `path` in `data` starting from the `t+1`th element to the end of the list.
    for result in results:
        print(result)
        
    #State: Output State: `t` is an integer, `data` is a list of strings, `index` is `2 * t`, `results` is a list containing `t` elements where each element is the result of `func_1(path)` for each `path` in `data` starting from the `t+1`th element to the end of the list, the loop has printed each element in the `results` list.
#Overall this is what the function does:The function processes a series of test cases, each containing an integer `t` (number of test cases), followed by an integer `n` (number of signs), and then `n` integers `a_1, a_2, ..., a_n` (periodicities of the signs). For each test case, it calculates the least common multiple (LCM) of the given periodicities and stores these LCM values in a list. Finally, it prints each LCM value from the list.


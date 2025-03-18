#State of the program right berfore the function call: path is a list of strings where each string is either '@', indicating a sign of the apocalypse, or '*', indicating an invalid or non-apocalyptic event.
def func_1(path):
    n = len(path)
    if (n == 0) :
        return 0
        #The program returns 0.
    #State: *`path` is a list of strings where each string is either '@' or '*', `n` is the length of `path`, and `n` is greater than 0
    dp = [0] * n
    if (path[0] == '@') :
        dp[0] = 1
    else :
        if (path[0] == '*') :
            dp[0] = -float('inf')
        #State: *`path` is a list of strings where each string is either '@' or '*', `n` is the length of `path` and is greater than 0, `dp` is a list of zeros with length `n` except `dp[0]` which is `-inf`, and the first element of `path` is '*'
    #State: *`path` is a list of strings where each string is either '@' or '*', `n` is the length of `path` and is greater than 0, `dp` is a list of zeros with length `n`. If the first element of `path` is '@', then `dp[0]` is 1. If the first element of `path` is '*', then `dp[0]` is `-inf`.
    if (n > 1) :
        if (path[1] == '*') :
            dp[1] = -float('inf')
        else :
            dp[1] = dp[0] + (1 if path[1] == '@' else 0)
        #State: *`path` is a list of strings where each string is either '@' or '*', `n` is the length of `path` and is greater than 1, `dp` is a list of zeros with length `n`. If the first element of `path` is '@', then `dp[0]` is 1. If the first element of `path` is '*', then `dp[0]` is `-inf`. If the second element of `path` is '*', then `dp[1]` is `-inf`. Otherwise, `dp[1]` is 2.
    #State: *`path` is a list of strings where each string is either '@' or '*', `n` is the length of `path` and is greater than 0, `dp` is a list of zeros with length `n`. If the first element of `path` is '@', then `dp[0]` is 1. If the first element of `path` is '*', then `dp[0]` is `-inf`. If `n` > 1 and the second element of `path` is '*', then `dp[1]` is `-inf`. If `n` > 1 and the second element of `path` is '@', then `dp[1]` is 2.
    for i in range(2, n):
        if path[i] == '*':
            dp[i] = -float('inf')
        else:
            dp[i] = max(dp[i - 1], dp[i - 2]) + (1 if path[i] == '@' else 0)
        
    #State: `dp` is a list where each element is either `-inf` or a positive integer. The value of `dp[i]` for `i >= 2` is determined by the maximum of `dp[i-1]` and `dp[i-2]`, plus 1 if `path[i]` is '@'. If `path[i]` is '*', `dp[i]` is `-inf`. The initial values of `dp[0]` and `dp[1]` remain unchanged.
    return max(x for x in dp if x > -float('inf'))
    #The program returns the maximum value from the list `dp` that is greater than `-inf`. This value is a positive integer, as `dp[i]` for `i >= 2` is either `-inf` or a positive integer, and the initial values of `dp[0]` and `dp[1]` are also either `-inf` or positive integers.
#Overall this is what the function does:The function `func_1` accepts a list of strings `path` where each string is either '@' (indicating a sign of the apocalypse) or '*' (indicating an invalid or non-apocalyptic event). It returns 0 if the list is empty or if all elements in the list are invalid (i.e., '*'). Otherwise, it returns the maximum positive integer representing the best possible outcome based on the path, calculated by summing the signs of the apocalypse while avoiding invalid events.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and data is a list of strings containing the input data for all test cases.
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
        
    #State: Output State: `t` is the integer value of the first element in `data`, `data` is a list of strings obtained by splitting the input read from `sys.stdin`, `index` is `2 * t + 1`, `results` is a list containing the results of `func_1(path)` for each `path` in `data` from the second element to the `2 * t`-th element, incrementing by 2.
    for result in results:
        print(result)
        
    #State: The loop has printed each element in the `results` list, one by one. The variables `t`, `data`, `index`, and `results` remain unchanged.
#Overall this is what the function does:The function `func_2` reads input from `sys.stdin`, processes a list of strings `data` containing input data for `t` test cases, where `t` is an integer such that 1 <= t <= 1000. It extracts paths from `data` and applies `func_1` to each path, storing the results in a list `results`. After processing all test cases, it prints each result in `results` to the standard output. The function does not return any value. After the function concludes, the variables `t`, `data`, `index`, and `results` remain unchanged, and the results of the test cases have been printed to the standard output.


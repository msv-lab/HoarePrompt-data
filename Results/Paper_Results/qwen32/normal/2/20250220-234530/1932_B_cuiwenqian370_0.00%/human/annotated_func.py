#State of the program right berfore the function call: path is a list of characters where each character can be either '@' or '*', representing different conditions in a sequence.
def func_1(path):
    n = len(path)
    if (n == 0) :
        return 0
        #The program returns 0
    #State: `path` is a list of characters where each character can be either '@' or '*', and `n` is the length of `path`. `n` is greater than 0
    dp = [0] * n
    if (path[0] == '@') :
        dp[0] = 1
    else :
        if (path[0] == '*') :
            dp[0] = -float('inf')
        #State: `path` is a list of characters where each character can be either '@' or '*', and `n` is the length of `path`. `n` is greater than 0; `dp` is a list of integers with `n` elements, where the first element is `-inf` if the condition `path[0] == '*'` is true, and the rest are initialized to 0. The first element of `path` is '*'.
    #State: `path` is a list of characters where each character can be either '@' or '*', and `n` is the length of `path`. `n` is greater than 0. `dp` is a list of integers with `n` elements. If the first character of `path` is '@', the first element of `dp` is 1 and the rest are 0. If the first character of `path` is '*', the first element of `dp` is `-inf` and the rest are 0.
    if (n > 1) :
        if (path[1] == '*') :
            dp[1] = -float('inf')
        else :
            dp[1] = dp[0] + (1 if path[1] == '@' else 0)
        #State: `path` is a list of characters where each character can be either '@' or '*', and `n` is the length of `path`. `n` is greater than 1. `dp` is a list of integers with `n` elements. If the first character of `path` is '@', the first element of `dp` is 1. If the second character of `path` is '*', the second element of `dp` is `-inf`; otherwise, it is 2 if the second character of `path` is '@' or 1 if the second character of `path` is '*'. If the first character of `path` is '*', the first element of `dp` is `-inf`. The second element of `dp` is `-inf` regardless of the second character of `path`. The rest of the elements in `dp` are 0.
    #State: `path` is a list of characters where each character can be either '@' or '*', and `n` is the length of `path`. `n` is greater than 0. `dp` is a list of integers with `n` elements. If `n` is 1, `dp` remains unchanged as per the precondition. If `n` is greater than 1, the first element of `dp` is 1 if the first character of `path` is '@', otherwise it is `-inf`. The second element of `dp` is `-inf` if the first character of `path` is '*', or if the second character of `path` is '*'; otherwise, it is 2 if the second character of `path` is '@' or 1 if the second character of `path` is '*'. The rest of the elements in `dp` are 0.
    for i in range(2, n):
        if path[i] == '*':
            dp[i] = -float('inf')
        else:
            dp[i] = max(dp[i - 1], dp[i - 2]) + (1 if path[i] == '@' else 0)
        
    #State: `dp` is a list where `dp[0]` is 1 if `path[0]` is '@' otherwise `-inf`, `dp[1]` is `-inf` if `path[0]` is '*' or `path[1]` is '*', otherwise 2 if `path[1]` is '@' or 1 if `path[1]` is '*', and for each `i` from 2 to `n-1`, `dp[i]` is `-inf` if `path[i]` is '*', otherwise `max(dp[i - 1], dp[i - 2]) + 1` if `path[i]` is '@' or `max(dp[i - 1], dp[i - 2])` if `path[i]` is '*'.
    return max(x for x in dp if x > -float('inf'))
    #The program returns the maximum value in the `dp` list that is greater than `-inf`.
#Overall this is what the function does:The function `func_1` takes a list of characters `path` where each character is either '@' or '*'. It returns 0 if the list is empty. Otherwise, it calculates a score based on the sequence of characters, where '@' contributes positively to the score and '*' results in a score of negative infinity for that position. The function returns the highest possible score from the sequence, ignoring any positions with a score of negative infinity.

#State of the program right berfore the function call: path is a string representing space-separated integers a_1, a_2, ..., a_n where each a_i is an integer such that 1 <= a_i <= 10^6, and n is an integer such that 1 <= n <= 100.
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
        
    #State: `path` is `'a_{1+2*t}'`; `input` is assigned the `sys.stdin.read` function; `data` is a list of strings ['a_1', 'a_2', ..., 'a_n']; `t` is the integer value of `data[0]`; `index` is `1 + 2*t`; `results` is `[func_1('a_3'), func_1('a_5'), ..., func_1('a_{1+2*(t-1)})]`.
    for result in results:
        print(result)
        
    #State: `path` is `'a_{1+2*t}'`, `input` is assigned the `sys.stdin.read` function, `data` is a list of strings `['1', 'a_2', ..., 'a_n']`, `t` is `1`, `index` is `3`, `results` is `[func_1('a_3'), func_1('a_5')]`.
#Overall this is what the function does:The function `func_2` reads input from standard input, which consists of multiple test cases. Each test case starts with an integer `n` followed by a string `path` containing `n` space-separated integers. For each test case, it processes the `path` using `func_1` and prints the result.


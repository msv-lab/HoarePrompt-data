#State of the program right berfore the function call: path is a non-empty list of strings where each string is either '@', '*', or a representation of a sign's periodicity. The length of path is at least 2.
def func_1(path):
    n = len(path)
    if (n == 0) :
        return 0
        #The program returns 0.
    #State: path is a non-empty list of strings where each string is either '@', '*', or a representation of a sign's periodicity. The length of path is at least 2, and `n` is equal to the length of `path`. `n` is not equal to 0.
    dp = [0] * n
    if (path[0] == '@') :
        dp[0] = 1
    else :
        if (path[0] == '*') :
            dp[0] = -float('inf')
        #State: `path` is a non-empty list of strings where each string is either '@', '*', or a representation of a sign's periodicity. The length of `path` is at least 2, and `n` is equal to the length of `path`. `n` is not equal to 0. `dp` is a list of length `n` filled with zeros, except if `path[0]` is '*', then `dp[0]` is `-inf`. The first element of `path` is not '@'.
    #State: *`path` is a non-empty list of strings where each string is either '@', '*', or a representation of a sign's periodicity. The length of `path` is at least 2, and `n` is equal to the length of `path`. `n` is not equal to 0. `dp` is a list of length `n`. If the first element of `path` is '@', then `dp[0]` is 1 and the rest of the elements in `dp` are zeros. If the first element of `path` is '*', then `dp[0]` is `-inf` and the rest of the elements in `dp` are zeros. Otherwise, `dp` is a list of length `n` filled with zeros.
    if (n > 1) :
        if (path[1] == '*') :
            dp[1] = -float('inf')
        else :
            dp[1] = dp[0] + (1 if path[1] == '@' else 0)
        #State: `path` is a non-empty list of strings where each string is either '@', '*', or a representation of a sign's periodicity. The length of `path` is at least 2, and `n` is equal to the length of `path`. `n` is not equal to 0 and is greater than 1. `dp` is a list of length `n`. If the first element of `path` is '@', then `dp[0]` is 1 and `dp[1]` is 2 if `path[1]` is '@', otherwise `dp[1]` is 1. If the first element of `path` is '*', then `dp[0]` is `-inf` and `dp[1]` is `-inf` if `path[1]` is '@', otherwise `dp[1]` is `-inf`. Otherwise, `dp[0]` is 0 and `dp[1]` is 1 if `path[1]` is '@', otherwise `dp[1]` is 0. The rest of the elements in `dp` are zeros. If the second element of `path` is '*', then `dp[1]` is `-inf`. If the second element of `path` is not '*', then the values of `dp[1]` are as described above.
    #State: *`path` is a non-empty list of strings where each string is either '@', '*', or a representation of a sign's periodicity. The length of `path` is at least 2, and `n` is equal to the length of `path`. `n` is not equal to 0. `dp` is a list of length `n`. If the first element of `path` is '@', then `dp[0]` is 1. If `n` > 1, `dp[1]` is 2 if `path[1]` is '@', otherwise `dp[1]` is 1. If the first element of `path` is '*', then `dp[0]` is `-inf`. If `n` > 1, `dp[1]` is `-inf` if `path[1]` is '@', otherwise `dp[1]` is `-inf`. If the first element of `path` is neither '@' nor '*', then `dp[0]` is 0. If `n` > 1, `dp[1]` is 1 if `path[1]` is '@', otherwise `dp[1]` is 0. The rest of the elements in `dp` are zeros. If the second element of `path` is '*', then `dp[1]` is `-inf`. If the second element of `path` is not '*', then the values of `dp[1]` are as described above.
    for i in range(2, n):
        if path[i] == '*':
            dp[i] = -float('inf')
        else:
            dp[i] = max(dp[i - 1], dp[i - 2]) + (1 if path[i] == '@' else 0)
        
    #State: `dp` is a list of length `n`. Each element in `dp` represents the maximum number of '@' signs that can be collected up to that index, considering the constraints imposed by '*' signs. If an element in `path` is '*', the corresponding element in `dp` is `-inf`. If an element in `path` is '@', the corresponding element in `dp` is the maximum value of the previous two elements in `dp` plus 1. If an element in `path` is a sign's periodicity (not '@' or '*'), the corresponding element in `dp` is the maximum value of the previous two elements in `dp`.
    return max(x for x in dp if x > -float('inf'))
    #The program returns the maximum value among the elements in the `dp` list that are greater than negative infinity.
#Overall this is what the function does:The function `func_1` accepts a parameter `path`, which is a non-empty list of strings where each string is either '@', '*', or a representation of a sign's periodicity, and the length of `path` is at least 2. It returns the maximum number of '@' signs that can be collected while traversing the `path`, with the constraint that encountering a '*' sign results in an immediate penalty represented by `-inf`. If the `path` is empty, the function returns 0. Otherwise, it returns the highest value in the `dp` list that is greater than `-inf`, which represents the optimal number of '@' signs that can be collected under the given constraints.

#State of the program right berfore the function call: None of the variables in the function signature are used in the function body. The function reads input from stdin and processes it, but the function signature itself does not provide any variables that are directly relevant to the problem description.
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
        
    #State: Output State: `data` is a list of strings obtained by splitting the input read from `sys.stdin`, `t` is the integer value of the first element in `data`, `index` is `1 + 2 * t`, `results` is a list containing the results of `func_1(path)` for each `path` in the input, where `path` is the string at every second position starting from index 1 in the `data` list.
    for result in results:
        print(result)
        
    #State: The `results` list remains unchanged, and all elements in `results` are printed to the console. The variables `data`, `t`, and `index` remain the same as in the initial state.
#Overall this is what the function does:The function `func_2` reads input from the standard input (stdin), processes it to extract a series of paths, and then applies the function `func_1` to each path. The results of these function calls are collected into a list and printed to the console, one result per line. The function does not return any value. After the function concludes, the `results` list contains the output of `func_1` for each path, and the variables `data`, `t`, and `index` are in the same state as described in the final annotation.


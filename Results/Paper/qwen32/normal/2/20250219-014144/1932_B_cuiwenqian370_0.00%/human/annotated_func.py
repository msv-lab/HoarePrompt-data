#State of the program right berfore the function call: path is a list of characters where each character can be either '@' or '*', representing different conditions in a sequence, and the length of path (n) is a non-negative integer.
def func_1(path):
    n = len(path)
    if (n == 0) :
        return 0
        #The program returns 0
    #State: `path` is a list of characters where each character can be either '@' or '*', representing different conditions in a sequence, and the length of `path` (n) is a non-negative integer greater than 0; `n` is the length of `path`.
    dp = [0] * n
    if (path[0] == '@') :
        dp[0] = 1
    else :
        if (path[0] == '*') :
            dp[0] = -float('inf')
        #State: `path` is a list of characters where each character can be either '@' or '*', representing different conditions in a sequence, and the length of `path` (n) is a non-negative integer greater than 0; `n` is the length of `path`; `dp` is a list of zeros with length `n` except the first element which is `-inf`. The first element of `path` is '*'
    #State: `path` is a list of characters where each character can be either '@' or '*', representing different conditions in a sequence, and the length of `path` (n) is a non-negative integer greater than 0; `n` is the length of `path`; `dp` is a list of zeros with length `n` except the first element which is 1 if the first element of `path` is '@', otherwise it is `-inf` if the first element of `path` is '*'
    if (n > 1) :
        if (path[1] == '*') :
            dp[1] = -float('inf')
        else :
            dp[1] = dp[0] + (1 if path[1] == '@' else 0)
        #State: `path` is a list of characters where each character can be either '@' or '*', representing different conditions in a sequence, and the length of `path` (n) is a non-negative integer greater than 1; `n` is the length of `path`. `dp` is a list where the first element is 1 if the first element of `path` is '@', otherwise it is `-inf`. If the second element of `path` is '*', the second element of `dp` is `-inf`; otherwise, the second element of `dp` is 2 if the first element of `path` is '@', otherwise it is `-inf`. All other elements of `dp` are 0.
    #State: `path` is a list of characters where each character can be either '@' or '*', representing different conditions in a sequence, and the length of `path` (n) is a non-negative integer greater than 0; `n` is the length of `path`. `dp` is a list where the first element is 1 if the first element of `path` is '@', otherwise it is `-inf`. If `n` is greater than 1, the second element of `dp` is `-inf` if the second element of `path` is '*', otherwise, it is 2 if the first element of `path` is '@', otherwise it is `-inf`. All other elements of `dp` are 0.
    for i in range(2, n):
        if path[i] == '*':
            dp[i] = -float('inf')
        else:
            dp[i] = max(dp[i - 1], dp[i - 2]) + (1 if path[i] == '@' else 0)
        
    #State: the final `dp` list after processing all elements of `path`.
    return max(x for x in dp if x > -float('inf'))
    #The program returns the maximum value from the `dp` list that is greater than negative infinity.
#Overall this is what the function does:The function `func_1` takes a list of characters `path` as input, where each character is either '@' or '*'. It returns 0 if the list is empty. Otherwise, it calculates a score based on the sequence of characters, treating '@' as a positive increment and '*' as an invalid state, and returns the highest possible score achievable without encountering an invalid state.

#State of the program right berfore the function call: path is a string representing space-separated integers a_1, a_2, ..., a_n where each a_i is a positive integer (1 <= a_i <= 10^6), and n is a positive integer (1 <= n <= 100) representing the number of signs.
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
        
    #State: `path` is `data[2*t]`; `data` is a list of strings `['a_1', 'a_2', ..., 'a_n']`; `t` is the integer value of `a_1`; `index` is `1 + 2*t`; `results` is a list containing the return values of `func_1(path)` for each iteration.
    for result in results:
        print(result)
        
    #State: The loop prints each element of the `results` list, completing all iterations.
#Overall this is what the function does:The function `func_2` reads input from standard input, processes multiple test cases, and for each test case, it applies `func_1` to a string of space-separated integers. It then prints the results of these applications.


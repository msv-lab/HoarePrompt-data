#State of the program right berfore the function call: path is a list or string consisting of characters, where each character can be either '@' or '*'.
def func_1(path):
    n = len(path)
    if (n == 0) :
        return 0
        #The program returns 0
    #State: `path` is a list or string consisting of characters, where each character can be either '@' or '*'; `n` is the length of `path` and `n` is greater than 0
    dp = [0] * n
    if (path[0] == '@') :
        dp[0] = 1
    else :
        if (path[0] == '*') :
            dp[0] = -float('inf')
        #State: `path` is a list or string consisting of characters, where each character can be either '@' or '*'; `n` is the length of `path` and `n` is greater than 0; `dp` is a list of zeros with length `n` except `dp[0]` which is `-inf` if the first character of `path` is '*'.
    #State: `path` is a list or string consisting of characters, where each character can be either '@' or '*'. `n` is the length of `path` and `n` is greater than 0. If the first character of `path` is '@', `dp` is a list where the first element is 1 and the remaining elements are zeros. If the first character of `path` is '*', `dp` is a list where the first element is `-inf` and the remaining elements are zeros.
    if (n > 1) :
        if (path[1] == '*') :
            dp[1] = -float('inf')
        else :
            dp[1] = dp[0] + (1 if path[1] == '@' else 0)
        #State: `path` is a list or string consisting of characters, where each character can be either '@' or '*'. `n` is the length of `path` and `n` is greater than 1. If the first character of `path` is '@', `dp` is a list where the first element is 1. If the second character of `path` is '*', the second element of `dp` is `-inf`; otherwise, it is 2. If the first character of `path` is '*', `dp` is a list where the first element is `-inf`. If the second character of `path` is '*', the second element of `dp` is `-inf`; otherwise, it is `-inf`. The remaining elements of `dp` are zeros.
    #State: `path` is a list or string consisting of characters, where each character can be either '@' or '*'. `n` is the length of `path` and `n` is greater than 0. If `n` is 1, `dp` remains as initialized: the first element is 1 if the first character of `path` is '@', otherwise it is `-inf`, and the remaining elements are zeros. If `n` is greater than 1, the first element of `dp` is 1 if the first character of `path` is '@', otherwise it is `-inf`. The second element of `dp` is `-inf` if the second character of `path` is '*', otherwise it is 2 if the first character of `path` is '@', or `-inf` if the first character of `path` is '*'. The remaining elements of `dp` are zeros.
    for i in range(2, n):
        if path[i] == '*':
            dp[i] = -float('inf')
        else:
            dp[i] = max(dp[i - 1], dp[i - 2]) + (1 if path[i] == '@' else 0)
        
    #State: dp array reflecting the maximum score possible up to each position in the path, with `-inf` at positions corresponding to '*' in the path.
    return max(x for x in dp if x > -float('inf'))
    #The program returns the maximum score possible from the dp array, excluding any positions that have a value of -inf.
#Overall this is what the function does:The function `func_1` takes a parameter `path`, which is a list or string of characters where each character can be either '@' or '*'. It returns 0 if the `path` is empty. Otherwise, it calculates and returns the maximum score possible by traversing the `path`, where each '@' contributes 1 to the score and each '*' results in an invalid position represented by `-inf`. The score is determined by considering the maximum score up to each position, excluding invalid positions.

#State of the program right berfore the function call: path is a string representing a sequence of space-separated integers where each integer a_i (1 ≤ a_i ≤ 10^6) represents the periodicity of a sign, and n is an integer (1 ≤ n ≤ 100) representing the number of signs.
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
        
    #State: `path` is the string value of the element at position `2 * t + 1` in `data`; `n` is the integer value of the element at position `2 * t` in `data`; `data` remains unchanged; `t` is the integer value of the first element in `data`; `index` is `2 * t + 1`; `results` contains `t` elements, each of which is the result of `func_1(path)` for each respective `path`.
    for result in results:
        print(result)
        
    #State: All elements in `results` have been printed. `data`, `t`, `path`, `n`, and `index` remain unchanged.
#Overall this is what the function does:The function `func_2` reads input from standard input, processes multiple test cases, and prints the result for each test case. Each test case consists of an integer `n` and a string `path`. The string `path` contains space-separated integers representing the periodicity of signs. For each test case, the function computes a result using another function `func_1` and prints this result.


#State of the program right berfore the function call: path is a string consisting of '@' and '*' characters, where '@' represents a valid sign and '*' represents an invalid sign or a gap that cannot contribute to forming a valid sequence of signs.
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
        #State: Postcondition: `path` is a string consisting of '@' and '*' characters, `n` is the length of `path`, `dp` is a list of `n` zeros. If the first character of `path` is '*', the first element of `dp` is `-inf`. Otherwise, the first element of `dp` remains `0`.
    #State: Postcondition: `path` is a string consisting of '@' and '*' characters, `n` is the length of `path`, and `dp` is a list of `n` zeros. If the first character of `path` is '@', the first element of `dp` is `1`. If the first character of `path` is '*', the first element of `dp` is `-inf`. Otherwise, the first element of `dp` remains `0`.
    if (n > 1) :
        if (path[1] == '*') :
            dp[1] = -float('inf')
        else :
            dp[1] = dp[0] + (1 if path[1] == '@' else 0)
        #State: Postcondition: `path` is a string consisting of '@' and '*' characters, `n` is the length of `path`, `dp` is a list of `n` elements where the first element is either `1` or `-inf` depending on the first character of `path`, and the second element of `dp` is `dp[0] + 1` if the second character of `path` is '@', otherwise `dp[1]` is `dp[0]`.
    #State: Postcondition: `path` is a string consisting of '@' and '*' characters, `n` is the length of `path`, and `dp` is a list of `n` elements. The first element of `dp` is either `1` or `-inf` depending on the first character of `path`. The second element of `dp` is `dp[0] + 1` if the second character of `path` is '@', otherwise `dp[1]` is `dp[0]`.
    for i in range(2, n):
        if path[i] == '*':
            dp[i] = -float('inf')
        else:
            dp[i] = max(dp[i - 1], dp[i - 2]) + (1 if path[i] == '@' else 0)
        
    #State: After the loop executes all iterations, `dp[i]` for each index `i` from 0 to `n-1` will be updated according to the rules specified in the loop body. Specifically, `dp[i]` will be `-float('inf')` if `path[i]` is '*', and otherwise, `dp[i]` will be the maximum of `dp[i - 1]` and `dp[i - 2]` plus 1 if `path[i]` is '@', or simply the maximum of `dp[i - 1]` and `dp[i - 2]` if `path[i]` is any other character. The final state of `dp` will reflect these updates for all characters in `path`.
    return max(x for x in dp if x > -float('inf'))
    #The program returns the maximum value among the elements in `dp` that are not equal to `-float('inf')`.
#Overall this is what the function does:The function `func_1` accepts a string `path` consisting of '@' and '*' characters. It calculates a dynamic programming array `dp` where each element depends on the previous elements based on the characters in `path`. If a character in `path` is '*', the corresponding `dp` element is set to `-inf`. If the character is '@', the `dp` element is incremented from the previous two elements. Finally, the function returns the maximum value among the `dp` elements that are not `-inf`. If no valid sequence exists, it returns 0.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 100, representing the number of signs, and path is a space-separated string containing n integers a_1, a_2, a_3, ..., a_n such that 1 ≤ a_i ≤ 10^6, representing the periodicities of the signs.
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
        
    #State: `t` must be 0 or less; `index` is increased by 51 (since 3 times 17 equals 51); `path` is the value of `data[index]`; `results` is a list with three additional elements which are the return values of `func_1(data[index])` for each iteration; `n` is the value of `data[index]`, `n` is an integer.
    for result in results:
        print(result)
        
    #State: `results` must have exactly three elements.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of an integer `t` (number of test cases), an integer `n` (number of signs), and a string `path` containing space-separated integers representing the periodicities of the signs. For each test case, it calls `func_1(path)` to process the `path` string and stores the result. After processing all test cases, it prints the results of `func_1` for each test case.


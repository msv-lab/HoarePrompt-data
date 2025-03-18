#State of the program right berfore the function call: path is a string consisting of characters '@' and '*', where the length of the string is at least 1.
def func_1(path):
    n = len(path)
    if (n == 0) :
        return 0
        #The program returns 0
    #State: `path` is a string consisting of characters '@' and '*', `n` is the length of `path`, and the length of `path` is not 0
    dp = [0] * n
    if (path[0] == '@') :
        dp[0] = 1
    else :
        if (path[0] == '*') :
            dp[0] = -float('inf')
        #State: Postcondition: `path` is a string consisting of characters '@' and '*', `n` is the length of `path`, and `dp` is a list of `n` zeros. If the first character of `path` is '*', the first element of `dp` is set to `-inf`.
    #State: Postcondition: `path` is a string consisting of characters '@' and '*', `n` is the length of `path`, and `dp` is a list of `n` zeros. If the first character of `path` is '@', the first element of `dp` is set to 1. If the first character of `path` is '*', the first element of `dp` is set to `-inf`.
    if (n > 1) :
        if (path[1] == '*') :
            dp[1] = -float('inf')
        else :
            dp[1] = dp[0] + (1 if path[1] == '@' else 0)
        #State: Postcondition: `path` is a string consisting of characters '@' and '*', `n` is the length of `path`, and `dp` is a list of `n` elements where:
        #- The first element of `dp` is either 1 (if the first character of `path` is '@') or `-inf` (if the first character of `path` is '*').
        #- The second element of `dp` is `-inf` if the second character of `path` is '*', otherwise it is `dp[0] + 1` if the second character of `path` is '@'.
    #State: Postcondition: `path` is a string consisting of characters '@' and '*', `n` is the length of `path`, and `dp` is a list of `n` elements where:
    #- The first element of `dp` is either 1 (if the first character of `path` is '@') or `-inf` (if the first character of `path` is '*').
    #- The second element of `dp` is `-inf` if the second character of `path` is '*', otherwise it is `dp[0] + 1` if the second character of `path` is '@'.
    for i in range(2, n):
        if path[i] == '*':
            dp[i] = -float('inf')
        else:
            dp[i] = max(dp[i - 1], dp[i - 2]) + (1 if path[i] == '@' else 0)
        
    #State: Output State: After the loop executes all the iterations, the variable `i` will be equal to `n`, meaning the loop has completed all its iterations up to the length of the `path` string. For each index `i` from 2 to `n-1`, the value of `dp[i]` will be determined based on the conditions specified within the loop. Specifically, if `path[i]` is '*', then `dp[i]` will be `-inf`. Otherwise, `dp[i]` will be the maximum of `dp[i-1]` and `dp[i-2]` plus 1 if `path[i]` is '@', or plus 0 if `path[i]` is '*'. All other variables in the precondition remain unchanged.
    #
    #In simpler terms, after running the loop through all iterations, `dp` will contain values that reflect the maximum possible sum of consecutive '@' characters, considering the constraints given by '*' characters in the `path` string.
    return max(x for x in dp if x > -float('inf'))
    #The program returns the maximum value among the elements in the `dp` list that are greater than negative infinity.
#Overall this is what the function does:The function `func_1` accepts a string `path` consisting of characters '@' and '*', where the length of the string is at least 1. It initializes a list `dp` to store intermediate results. Depending on the first character of `path`, it sets the initial value of `dp[0]`. Then, it iterates through the remaining characters of `path`, updating `dp` based on whether the current character is '@' or '*'. Finally, it returns the maximum value among the elements in `dp` that are greater than negative infinity, or 0 if no such value exists.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, representing the number of test cases. n is an integer such that 1 ≤ n ≤ 100, representing the number of signs for each test case. path is a string containing n space-separated integers a_1, a_2, a_3, ..., a_n such that 1 ≤ a_i ≤ 10^6, representing the periodicities of the signs for each test case.
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
        
    #State: Output State: `index` is 10, `t` is the first element of `data` converted to an integer and decremented by 3, `n` is the eighth element of `data` converted to an integer, `path` is the ninth element of `data` converted to an integer, `results` now contains the return value of `func_1(path)` appended to its previous contents.
    #
    #This output state indicates that after the loop has executed all its iterations (as determined by the initial value of `t` being decremented by 3 for each iteration), the `index` variable will be at 10 (since it increments by 2 with each iteration of the loop). The `t` variable will be the original value minus 3, as it is decremented by 1 in each iteration of the loop. The `n` variable will be the sixth element of the `data` list converted to an integer, and the `path` variable will be the tenth element of the `data` list converted to an integer. The `results` list will contain the cumulative results of calling `func_1(path)` for each iteration of the loop.
    for result in results:
        print(result)
        
    #State: `index` is 10, `t` is the first element of `data` converted to an integer and decremented by 6, `n` is the eighth element of `data` converted to an integer, `path` is the ninth element of `data` converted to an integer, `results` contains the cumulative results of calling `func_1(path)` for each iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a number of signs with specific periodicities. It reads input from stdin, extracts the necessary data for each test case, calls another function `func_1` to process the periodicities, and stores the results. Finally, it prints the results for each test case. The function does not return any value.


#State of the program right berfore the function call: n is an integer representing the length of the binary string s, and s is a string of length n consisting only of the characters '0' and '1'.
def func_1(n, s):
    zero_count = s.count('0')
    if (zero_count == 0) :
        return n
        #The program returns `n`, which represents the length of the binary string `s`
    #State of the program after the if block has been executed: `n` is an integer representing the length of the binary string `s`, `s` is a string of length `n` consisting only of the characters '0' and '1', and `zero_count` is the count of '0's in `s`. The zero_count is not equal to 0
    max_k = 1
    for k in range(1, n + 1):
        if zero_count % k == 0:
            max_k = k
        
    #State of the program after the  for loop has been executed: `n` is an integer, `s` is a binary string of length `n`, `zero_count` is the count of '0's in `s`, and `max_k` is the largest integer `k` such that `zero_count % k == 0`, or 1 if no such `k` exists.
    return max_k
    #The program returns `max_k`, which is the largest integer `k` such that `zero_count % k == 0`, or 1 if no such `k` exists
#Overall this is what the function does:The function `func_1` accepts two parameters: `n` (an integer representing the length of the binary string `s`) and `s` (a string of length `n` consisting only of '0' and '1'). It first checks if the string `s` contains any '0's. If it does not contain any '0's, it returns the length `n` of the string. Otherwise, it calculates the largest integer `k` such that the count of '0's in `s` is divisible by `k`. If no such `k` exists, it returns 1. The function returns either `n` or the calculated `max_k` based on the conditions described.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 5000, and s is a binary string of length n consisting of '0's and '1's.
def func_2():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        
        s = data[index + 1]
        
        index += 2
        
        result = func_1(n, s)
        
        results.append(result)
        
    #State of the program after the  for loop has been executed: `data` is a list of strings, `t` is 0, `index` is `2 * data[0] + 1`, `results` is a list containing the return values of `func_1(n, s)` for each iteration.
    for res in results:
        print(res)
        
    #State of the program after the  for loop has been executed: `data` is a list of strings, `t` is 0, `index` is `2 * data[0] + 1`, `results` is a list containing the return values of `func_1(n, s)` for each iteration, `res` is the last element from `results`, and `res` is printed.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer `t` (number of cases), an integer `n` (length of a binary string `s`), and a binary string `s` itself. It then processes each test case by calling `func_1(n, s)` to obtain a result for each case, stores these results in a list `results`, and finally prints each result. The function ensures that it correctly handles the input for up to 10,000 test cases, with each binary string having a maximum length of 5,000 characters. If the input format is incorrect or incomplete, the function will still attempt to process as much valid input as possible.


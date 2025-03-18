#State of the program right berfore the function call: n is an integer such that 1 <= n <= 20, a, b, and c are strings of length n consisting of lowercase Latin letters.
def func_1(n, a, b, c):
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            return 'YES'
        
    #State: Output State: The loop has executed all its iterations, meaning `i` is now equal to `n`. During these iterations, the condition `a[i] != c[i] and b[i] != c[i]` was never met for any `i` from `0` to `n-1`. Therefore, the function does not return 'YES' during the loop's execution. As a result, the function continues until the loop completes without returning 'YES', implying that for every `i` in the range `0` to `n-1`, at least one of the following holds true: `a[i] == c[i]` or `b[i] == c[i]`.
    #
    #The final output state is that the function has completed all its iterations without returning 'YES', and for each index `i` from `0` to `n-1`, the condition `a[i] == c[i]` or `b[i] == c[i]` is satisfied.
    return 'NO'
    #The program returns 'NO', indicating that for every index i from 0 to n-1, the condition a[i] == c[i] or b[i] == c[i] is satisfied, and the function did not return 'YES' during its execution.
#Overall this is what the function does:The function accepts three parameters: `n`, `a`, and `b`, where `n` is an integer between 1 and 20, and `a` and `b` are strings of length `n` consisting of lowercase Latin letters. It also accepts a parameter `c`, which is a string of length `n` consisting of lowercase Latin letters. The function checks if for every index `i` from 0 to `n-1`, either `a[i] == c[i]` or `b[i] == c[i]` is true. If it finds such a pair, it returns 'YES'. If it goes through all indices without finding any such pair, it returns 'NO'.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, n is an integer such that 1 ≤ n ≤ 20, a, b, and c are strings of exactly n lowercase Latin letters.
def func_2():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        
        a = input().strip()
        
        b = input().strip()
        
        c = input().strip()
        
        results.append(func_1(n, a, b, c))
        
    #State: Output State: `t` must be equal to 0, `n` is an integer input stripped of leading and trailing whitespace, `a` is the final input string stripped of leading and trailing whitespace, `b` is the final input string stripped of leading trailing whitespace, `c` is the final input string stripped of leading and trailing whitespace, `results` is a list containing the results of `func_1(n, a, b, c)` for each iteration from 1 to `t`, `_` is `t`.
    #
    #This means that after all iterations of the loop have finished, `t` will be 0 because it decreases by 1 with each iteration until it reaches 0. The values of `n`, `a`, `b`, and `c` will be the last inputs provided during the loop's execution. The `results` list will contain the outputs of `func_1(n, a, b, c)` for each of the `t` iterations.
    for result in results:
        print(result)
        
    #State: t is 0, n is an integer input stripped of leading and trailing whitespace, a is the final input string stripped of leading and trailing whitespace, b is the final input string stripped of leading and trailing whitespace, c is the final input string stripped of leading and trailing whitespace, results is a list containing the results of func_1(n, a, b, c) for each iteration from 1 to t, _ is t.
#Overall this is what the function does:The function reads multiple sets of inputs, where each set consists of an integer \( t \), an integer \( n \), and three strings \( a \), \( b \), and \( c \). For each set, it calls another function `func_1(n, a, b, c)` and stores the result. After processing all sets, it prints the results of these function calls. The final state of the program includes \( t \) being 0, and the variables \( n \), \( a \), \( b \), and \( c \) holding the last set of inputs provided.


#State of the program right berfore the function call: n is an integer such that 1 <= n <= 20, a, b, and c are strings of length n consisting of lowercase Latin letters.
def func_1(n, a, b, c):
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            return 'YES'
        
    #State: Output State: The loop has executed all its iterations, meaning `i` has reached `n`. If during any iteration from `i = 0` to `i = n-1`, both conditions `a[i] != c[i]` and `b[i] != c[i]` were met simultaneously, the function would have returned 'YES' before completing all iterations. Since no such simultaneous mismatch was found in any of the iterations, the function will return 'NO' after completing all iterations.
    #
    #In natural language: After all iterations of the loop have finished, the output will be 'NO', indicating that there was no index `i` where both `a[i]` and `b[i]` were different from `c[i]` simultaneously.
    return 'NO'
    #The program returns 'NO', indicating that there was no index i where both a[i] and b[i] were different from c[i] simultaneously after all iterations of the loop have finished.
#Overall this is what the function does:The function accepts three parameters: `n` (an integer between 1 and 20), `a` (a string of length `n` consisting of lowercase Latin letters), `b` (a string of length `n` consisting of lowercase Latin letters), and `c` (a string of length `n` consisting of lowercase Latin letters). It checks each index `i` from `0` to `n-1` to see if both `a[i]` and `b[i]` are different from `c[i]`. If such an index is found, it returns 'YES'. If no such index exists after checking all indices, it returns 'NO'.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 20, and a, b, c are strings of length n consisting of lowercase Latin letters.
def func_2():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        
        a = input().strip()
        
        b = input().strip()
        
        c = input().strip()
        
        results.append(func_1(n, a, b, c))
        
    #State: After the loop executes all iterations, `t` must be greater than 0, `results` is a list containing the result of `func_1(n, a, b, c)` for each iteration, `a` is the stripped input string from the last iteration, `b` is the stripped input string from the last iteration, and `c` is the stripped input string from the last iteration.
    for result in results:
        print(result)
        
    #State: Output State: `results` is a list that can be fully iterated over, containing the results of `func_1(n, a, b, c)` for each iteration, `n` is initialized and will have been decremented to 0 or a negative value, `a` is the stripped input string from the last iteration, `b` is the stripped input string from the last iteration, `c` is the stripped input string from the last iteration.
    #
    #This means that after all iterations of the loop have finished, `results` will contain the outputs of the function `func_1(n, a, b, c)` for every iteration. The variable `n` will have reached 0 or a negative value as it was likely being decremented in each iteration. Variables `a`, `b`, and `c` will hold the stripped input strings from the last iteration of the loop.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `n`, followed by three strings `a`, `b`, and `c`, and calls another function `func_1(n, a, b, c)`. It collects the results of these function calls into a list and prints each result. After processing all test cases, the function ensures that the list `results` contains the outputs of `func_1` for each test case, while the variables `n`, `a`, `b`, and `c` are left in their final states from the last test case.


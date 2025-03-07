#State of the program right berfore the function call: n is a positive integer, a, b, and c are strings of length n consisting of lowercase Latin letters.
def func_1(n, a, b, c):
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            return 'YES'
        
    #State: The loop has completed all iterations, `i` is `n-1`, and either `a[i]` is equal to `c[i]` or `b[i]` is equal to `c[i]` for all `i` from 0 to `n-1`. If at any point both `a[i]` and `b[i]` are not equal to `c[i]`, the program returns 'YES'. Otherwise, the program does not return 'YES'.
    return 'NO'
    #The program returns 'NO'
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and three strings `a`, `b`, and `c` of length `n` consisting of lowercase Latin letters. It returns 'YES' if at any index `i` (0 ≤ i < n), both `a[i]` and `b[i]` are different from `c[i]`. Otherwise, it returns 'NO' if for every index `i` (0 ≤ i < n), at least one of `a[i]` or `b[i]` matches `c[i]`.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, n is an integer such that 1 <= n <= 20, and a, b, c are strings of length n consisting of lowercase Latin letters.
def func_2():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        
        a = input().strip()
        
        b = input().strip()
        
        c = input().strip()
        
        results.append(func_1(n, a, b, c))
        
    #State: `t` must be greater than or equal to the number of iterations, `_` is `t-1`, `n` is an input integer with leading and trailing whitespace removed, `a` is a new input string with leading and trailing whitespace removed, `b` is a new input string with leading and trailing whitespace removed, `c` is a new input string with leading and trailing whitespace removed, `results` is a list that includes the value returned by `func_1(n, a, b, c)` `t` times.
    for result in results:
        print(result)
        
    #State: `t` must be greater than or equal to the number of iterations, `_` is `t-1`, `n` is an input integer with leading and trailing whitespace removed, `a` is a new input string with leading and trailing whitespace removed, `b` is a new input string with leading and trailing whitespace removed, `c` is a new input string with leading and trailing whitespace removed, `results` is a list that includes the value returned by `func_1(n, a, b, c)` `t` times, `results` must have `t` elements, and all elements in `results` have been printed.
#Overall this is what the function does:The function `func_2` reads an integer `t` from the input, where `1 <= t <= 1000`, representing the number of test cases. For each test case, it reads an integer `n` and three strings `a`, `b`, and `c`, each of length `n` and consisting of lowercase Latin letters. It then calls `func_1` with these parameters and appends the result to a list `results`. After processing all test cases, it prints each element in `results`. The final state of the program is that `t` test cases have been processed, and the results of calling `func_1` for each test case have been printed.


#State of the program right berfore the function call: n is a positive integer (1 <= n <= 20), a, b, and c are strings of length n consisting of lowercase Latin letters.
def func_1(n, a, b, c):
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            return 'YES'
        
    #State: `n` is a positive integer (1 <= n <= 20), `i` is `n-1`, `a`, `b`, and `c` are strings of length n consisting of lowercase Latin letters. If for any index `i` from 0 to `n-1`, `a[i]` is not equal to `c[i]` and `b[i]` is not equal to `c[i]`, the program returns 'YES'. Otherwise, the program does not return 'YES'.
    return 'NO'
    #The program returns 'NO'
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` (1 <= n <= 20) and three strings `a`, `b`, and `c` of length `n` consisting of lowercase Latin letters. It returns 'YES' if, for any index `i` from 0 to `n-1`, `a[i]` is not equal to `c[i]` and `b[i]` is not equal to `c[i]`. Otherwise, it returns 'NO'.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, representing the number of test cases.
def func_2():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        
        a = input().strip()
        
        b = input().strip()
        
        c = input().strip()
        
        results.append(func_1(n, a, b, c))
        
    #State: `t` is an integer such that 0 < t <= 1000, `results` is a list containing the results of `func_1(n, a, b, c)` appended `t` times, `n` is an input integer with leading and trailing whitespace removed, `a` is a string input by the user with leading and trailing whitespace removed, `b` is a string input by the user with leading and trailing whitespace removed, `c` is a string input by the user with leading and trailing whitespace removed.
    for result in results:
        print(result)
        
    #State: `t` is an integer such that 0 < t <= 1000, `results` is a list containing the results of `func_1(n, a, b, c)` appended `t` times and has been fully iterated, `n` is an input integer with leading and trailing whitespace removed, `a` is a string input by the user with leading and trailing whitespace removed, `b` is a string input by the user with leading and trailing whitespace removed, `c` is a string input by the user with leading and trailing whitespace removed.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer `t` from user input, where 1 <= t <= 1000, representing the number of test cases. For each test case, it reads three additional inputs: an integer `n` and two strings `a` and `b`, all with leading and trailing whitespace removed. It then calls `func_1` with these inputs and appends the result to a list `results`. After processing all test cases, it prints each result in the `results` list. The final state of the program is that `t` is an integer such that 0 < t <= 1000, `results` is a list containing the results of `func_1` for each test case, and the list has been fully iterated and printed.


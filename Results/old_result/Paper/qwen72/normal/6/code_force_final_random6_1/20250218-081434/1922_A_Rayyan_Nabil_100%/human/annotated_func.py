#State of the program right berfore the function call: n is a positive integer, a, b, and c are strings of length n consisting of lowercase Latin letters.
def func_1(n, a, b, c):
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            return 'YES'
        
    #State: `n` is a positive integer, `i` is `n-1`, and `a`, `b`, and `c` are strings of length `n` consisting of lowercase Latin letters. The loop has checked each character from index 0 to index `n-1`. If at any index `i`, `a[i]` and `b[i]` are both not equal to `c[i]`, the program returns 'YES'. If no such index is found, the program does not return anything.
    return 'NO'
    #The program returns 'NO'
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and three strings `a`, `b`, and `c` of length `n` consisting of lowercase Latin letters. It checks if there is any index `i` (from 0 to `n-1`) where both `a[i]` and `b[i]` are different from `c[i]`. If such an index is found, the function returns 'YES'. If no such index is found, the function returns 'NO'.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, representing the number of test cases.
def func_2():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        
        a = input().strip()
        
        b = input().strip()
        
        c = input().strip()
        
        results.append(func_1(n, a, b, c))
        
    #State: `t` is an input integer such that 1 <= t <= 1000, `results` is a list containing `t` results, each result being the output of `func_1(n, a, b, c)` for each iteration, `_` is a placeholder variable that has been incremented `t` times, `n` is the last input integer, `a` is the last stripped input string, `b` is the last stripped input string, `c` is the last stripped input string.
    for result in results:
        print(result)
        
    #State: `t` is an input integer such that 1 <= t <= 1000, `results` is a list containing `t` results, each result being the output of `func_1(n, a, b, c)` for each iteration, `result` is the last element of `results`
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer `t` from the input, where `1 <= t <= 1000`, representing the number of test cases. For each test case, it reads three additional inputs: an integer `n`, and two strings `a` and `b`, and a third string `c`. It then calls `func_1` with these inputs and appends the result to a list `results`. After processing all test cases, it prints each result in the `results` list. The final state of the program is that `t` is an integer such that `1 <= t <= 1000`, `results` is a list containing `t` results, and each result is the output of `func_1` for the corresponding test case.


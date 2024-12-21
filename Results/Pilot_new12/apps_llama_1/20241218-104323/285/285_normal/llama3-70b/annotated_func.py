#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 10^9.
def func():
    n = int(input())
    for a in range(n // 1234567 + 1):
        for b in range((n - a * 1234567) // 123456 + 1):
            c = (n - a * 1234567 - b * 123456) // 1234
            if a * 1234567 + b * 123456 + c * 1234 == n:
                print('YES')
                exit()
        
    #State of the program after the  for loop has been executed: `n` is an integer, `a` is either `n // 1234567` if the loop completes all iterations without finding a solution or the value of `a` when the condition `a * 1234567 + b * 123456 + c * 1234 == n` is satisfied if the program exits, `b` and `c` are defined and hold values corresponding to `a` if the program exits, or not defined if the loop completes without finding a solution.
    print('NO')
#Overall this is what the function does:The function reads a positive integer `n` from user input and attempts to find a combination of integers `a`, `b`, and `c` such that `n` can be expressed as `a * 1234567 + b * 123456 + c * 1234`. If such a combination is found, the function immediately prints 'YES' and exits. If no combination is found after iterating over all possible values of `a` and `b`, the function prints 'NO'. The function does not accept any parameters and does not return a value. After execution, the program's state will be one of two possible outcomes: either 'YES' will have been printed if a suitable combination was found, or 'NO' will have been printed if no combination was found. Note that the function's input range is limited by the annotation to 1 <= n <= 10^9, but this is not explicitly enforced by the code.


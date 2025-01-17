#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10, and s is a string of length n consisting of characters 'W' and 'B', where at least one character is 'B'.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        b = input()
        
        c = str(b[-1::-1])
        
        if c.count('B') > 1:
            print(a - c.index('B') - b.index('B'))
        else:
            print(a)
        
    #State of the program after the  for loop has been executed: `t` is a positive integer such that \(1 \leq t \leq 10^4\), `n` is a positive integer such that \(1 \leq n \leq 10\), `s` is a string of length `n` consisting of characters 'W' and 'B' with at least one 'B', `a` is an integer entered by the user, `b` is the string entered by the user, `c` is the reversed string of `b`. After all iterations of the loop, if the count of 'B' in `c` is greater than 1 for any iteration, the output will be the difference `a - c.index('B') - b.index('B')` for that iteration, otherwise, `a` will be printed for all iterations.
#Overall this is what the function does:The function processes multiple test cases, each containing a positive integer `t`, a positive integer `n`, and a string `s` of length `n` consisting of characters 'W' and 'B' with at least one 'B'. For each test case, it reads an integer `a` and a string `b` (which is the same as `s`), reverses the string `b`, and checks if the count of 'B' characters in the reversed string `c` is greater than 1. If it is, the function prints `a - c.index('B') - b.index('B')`. If the count is not greater than 1, it simply prints `a`. There is no explicit return value; the function prints the result for each test case. Potential edge cases include when `b` contains only one 'B' or no 'B', in which case the function will always print `a`. Additionally, the function assumes that the input constraints are met (`1 ≤ t ≤ 10^4`, `1 ≤ n ≤ 10`, and `s` contains at least one 'B'), and it does not handle cases where these constraints might not be satisfied.


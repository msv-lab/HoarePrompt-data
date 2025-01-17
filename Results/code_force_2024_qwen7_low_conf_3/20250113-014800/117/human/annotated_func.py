#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 10, and s is a string of length n consisting of characters 'W' and 'B', where 'B' indicates a black cell and 'W' indicates a white cell, and it is guaranteed that at least one cell in s is black.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        b = input()
        
        c = str(b[-1::-1])
        
        if c.count('B') > 1:
            print(a - c.index('B') - b.index('B'))
        else:
            print(a)
        
    #State of the program after the  for loop has been executed: `t` is at least 1, `n` is an integer in the range [1, 10], `s` is a string of length `n` containing characters 'W' and 'B' and at least one 'B', `a` is the final integer value entered by the user across all iterations, `b` is the final user's input across all iterations, `c` is the reversed version of `b`. If the count of 'B' in `c` is greater than 1, the final output of the print statement is `a - c.index('B') - b.index('B')`. Otherwise, the final value of `a` is printed.
#Overall this is what the function does:The function processes multiple test cases, where each test case involves an integer \(a\) and a string \(b\) of length \(n\) (where \(1 \leq n \leq 10\)) consisting of characters 'W' and 'B'. For each test case, the function reverses the string \(b\) and counts the occurrences of 'B'. If the count of 'B' is greater than 1, the function calculates and prints \(a - c.index('B') - b.index('B')\), where \(c\) is the reversed version of \(b\). If the count of 'B' is not greater than 1, the function simply prints \(a\). The function does not explicitly accept any parameters but operates on variables derived from user input. After the function concludes, it outputs a series of values based on the conditions described above. Potential edge cases include scenarios where the string \(b\) contains only one 'B' or no 'B' at all, which would result in the original value of \(a\) being printed.


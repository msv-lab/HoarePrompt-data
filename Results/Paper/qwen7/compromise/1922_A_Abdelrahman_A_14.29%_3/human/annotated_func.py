#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 20. a, b, and c are strings consisting of exactly n lowercase Latin letters.
def func():
    tests = int(input())
    for i in range(tests):
        slength = int(input())
        
        a = input()
        
        b = input()
        
        c = input()
        
        no = True
        
        if c == a or c == b:
            no = False
            print('NO')
        else:
            for x in c:
                if x not in a and x not in b:
                    print('YES')
                    no = False
                    break
        
        if no:
            print('NO')
        
    #State: Output State: `tests` must be greater than 0, `i` is the total number of iterations the loop executed (which is equal to `tests`), `slength` is an input integer, `a` is an input string, `b` is an input string, `c` is a string (neither `a` nor `b`), `no` is False, and `x` is the last character in `c` (if the loop breaks due to a character not being in `a` or `b`).
    #
    #Explanation: After all iterations of the loop have finished, the variable `i` will be equal to the total number of iterations, which is `tests`. The variable `no` will be set to `False` because the loop will eventually find a string `c` that does not contain any character that is not present in either `a` or `b`, or it will encounter a condition where `c` matches `a` or `b`, making `no` False before the loop completes all iterations. All other variables (`slength`, `a`, `b`, and `c`) will retain their final values from the last iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads three strings \(a\), \(b\), and \(c\) of length \(n\), where \(1 \leq n \leq 20\). It then checks if \(c\) contains any character that is not present in either \(a\) or \(b\). If \(c\) matches \(a\) or \(b\), or if \(c\) contains only characters from \(a\) and \(b\), it prints 'NO'. Otherwise, it prints 'YES'. The function does not return any value but prints the result for each test case.


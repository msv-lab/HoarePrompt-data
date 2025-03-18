#State of the program right berfore the function call: The function `func` is intended to process multiple test cases. Each test case includes an integer n (1 ≤ n ≤ 20) and three strings a, b, and c, each of length n and consisting of lowercase Latin letters. The integer t (1 ≤ t ≤ 1000) represents the number of test cases.
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
        
    #State: `i` is `tests - 1`, `tests` must be greater than 0, `slength` is an input integer, `a` is a new input string, `b` is a new input string, `c` is a new input string. If `c` is not equal to `a` or `b`, and all characters in `c` are found in `a` or `b`, then `no` is True. Otherwise, `no` is False.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` and three strings `a`, `b`, and `c` of length `n`. It checks if `c` is either equal to `a` or `b`, or if `c` contains at least one character that is not present in either `a` or `b`. If `c` is equal to `a` or `b`, or if all characters in `c` are found in both `a` and `b`, it prints 'NO'. Otherwise, it prints 'YES'. After processing all test cases, the function concludes without returning any value.


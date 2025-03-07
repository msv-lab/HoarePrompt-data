#State of the program right berfore the function call: t is an integer where 1 <= t <= 1000, n is an integer where 1 <= n <= 20, and a, b, c are strings of length n consisting of lowercase Latin letters.
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
        
    #State: `t` is an integer where 1 <= t <= 1000, `n` is an integer where 1 <= n <= 20, `a` is an input string of length `n` consisting of lowercase Latin letters, `b` is an input string of length `n` consisting of lowercase Latin letters, `c` is an input string of length `n` consisting of lowercase Latin letters, `tests` is the number of iterations the loop has executed, `i` is `tests - 1`, `slength` is an input integer. For each iteration, if `c` is equal to `a` or `b`, or if all characters in `c` are present in either `a` or `b`, `no` is True and 'NO' is printed. Otherwise, `no` is False and 'YES' is printed.
#Overall this is what the function does:The function `func` reads multiple sets of inputs from the user, each set consisting of an integer `slength` and three strings `a`, `b`, and `c` of length `slength`. For each set, it checks if `c` is equal to `a` or `b`, or if any character in `c` is not present in either `a` or `b`. If `c` is equal to `a` or `b`, or if all characters in `c` are present in both `a` and `b`, it prints 'NO'. Otherwise, it prints 'YES'. The function does not return any value. After the function concludes, the variables `tests`, `i`, `slength`, `a`, `b`, and `c` will reflect the state of the last iteration, and the number of 'YES' or 'NO' outputs will match the number of test cases `t`.


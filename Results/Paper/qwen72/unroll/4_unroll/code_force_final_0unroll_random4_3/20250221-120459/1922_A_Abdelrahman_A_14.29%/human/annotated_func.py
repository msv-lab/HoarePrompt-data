#State of the program right berfore the function call: The function should take four parameters: an integer t (1 ≤ t ≤ 1000) representing the number of test cases, and for each test case, an integer n (1 ≤ n ≤ 20) representing the length of the strings, and three strings a, b, and c, each consisting of exactly n lowercase Latin letters.
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
        
    #State: The loop will execute `tests` times, and for each test case, it will read `slength`, `a`, `b`, and `c` from the input. If `c` is equal to `a` or `b`, or if any character in `c` is not present in either `a` or `b`, it will print 'NO' or 'YES' respectively. After all iterations, the variables `i`, `slength`, `a`, `b`, and `c` will be in their final states corresponding to the last test case, and the variable `no` will be `True` if the last test case did not print 'YES', otherwise it will be `False`. The variable `tests` will remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and three strings `a`, `b`, and `c` of length `n` consisting of lowercase Latin letters. The function checks if `c` is equal to `a` or `b`, or if any character in `c` is not present in either `a` or `b`. If either condition is true, it prints 'NO'; otherwise, it prints 'YES'. After processing all test cases, the function does not return any value, but the final state of the program includes the variables `i`, `slength`, `a`, `b`, and `c` corresponding to the last test case, and the variable `no` will be `False` if any test case printed 'YES', otherwise it will be `True`. The variable `tests` remains unchanged.


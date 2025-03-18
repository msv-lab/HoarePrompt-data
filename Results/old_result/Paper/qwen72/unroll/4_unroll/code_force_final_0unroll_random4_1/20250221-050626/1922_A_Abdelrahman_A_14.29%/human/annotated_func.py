#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 20, and a, b, c are strings of length n consisting of lowercase Latin letters.
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
        
    #State: The values of `n`, `a`, `b`, and `c` remain unchanged, and `tests` is decremented by the number of iterations the loop has executed. The loop prints 'NO' if `c` is equal to `a` or `b`, or if all characters in `c` are present in both `a` and `b`. It prints 'YES' if at least one character in `c` is not present in either `a` or `b`.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. It reads an integer `tests` from the input, indicating the number of test cases to process. For each test case, it reads three strings `a`, `b`, and `c` of length `n` (where `1 ≤ n ≤ 20` and the strings consist of lowercase Latin letters). The function checks if `c` is equal to `a` or `b`, or if all characters in `c` are present in both `a` and `b`. If either condition is true, it prints 'NO'. If at least one character in `c` is not present in either `a` or `b`, it prints 'YES'. After processing all test cases, the function concludes, and the values of `n`, `a`, `b`, and `c` remain unchanged.


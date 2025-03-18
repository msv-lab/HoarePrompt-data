#State of the program right berfore the function call: start and end are integers such that start <= end, and they represent the range of folder names to be processed, where folder names are expected to be numeric.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        a = input()
        
        count = a.count('1')
        
        if count == 0:
            print('YES')
        elif count > 2 and count % 2 == 0:
            print('YES')
        elif count == 2:
            if a[a.index('1') + 1] != '1':
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
        
    #State: `start` and `end` are integers such that `start` <= `end`, `t` is greater than or equal to the number of iterations, `i` is `t - 1`, `n` is an input integer, `a` is the last input string, and `count` is the number of occurrences of '1' in the last `a`. The state of the variables `start` and `end` remains unchanged, and the state of `n`, `a`, and `count` is determined by the last iteration of the loop.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any values. It reads an integer `t` from the user, which represents the number of test cases. For each test case, it reads an integer `n` and a string `a` from the user. The function then checks the string `a` for the number of occurrences of the character '1'. If the count of '1's is 0, greater than 2 and even, or exactly 2 with the two '1's not adjacent, it prints 'YES'. Otherwise, it prints 'NO'. The function processes `t` test cases and prints the result for each one. The variables `start` and `end` mentioned in the annotations are not used in the function and do not affect its behavior.


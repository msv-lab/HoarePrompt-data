#State of the program right berfore the function call: start and end are integers such that 0 <= start <= end.
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
            if a.index('1') and a[a.index('1') + 1] != '1':
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
        
    #State: The values of `start` and `end` remain unchanged, and `t` is decremented by the number of iterations the loop has executed. The loop itself does not modify any of these variables, but it processes `t` inputs, each time reading an integer `n` and a string `a`, and prints 'YES' or 'NO' based on the conditions specified in the loop.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. It reads an integer `t` from the user, indicating the number of test cases. For each test case, it reads an integer `n` and a string `a` from the user. The function then checks the count of '1's in the string `a` and prints 'YES' or 'NO' based on the following conditions: if the count is 0, greater than 2 and even, or exactly 2 with the two '1's not adjacent, it prints 'YES'; otherwise, it prints 'NO'. The function processes `t` test cases and prints the result for each one. The state of the program after the function concludes is that `t` test cases have been processed, and the output for each test case has been printed.


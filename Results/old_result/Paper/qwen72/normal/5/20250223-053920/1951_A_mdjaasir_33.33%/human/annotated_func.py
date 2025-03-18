#State of the program right berfore the function call: start and end are integers where 0 <= start <= end.
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
        
    #State: The values of `start` and `end` remain unchanged, and `t` is decremented by the number of iterations that the loop has executed. The loop itself does not modify these variables, but it processes `t` inputs and prints 'YES' or 'NO' based on the conditions specified in the loop body.
#Overall this is what the function does:The function does not accept any parameters and does not return any value. It reads an integer `t` from the user input, which represents the number of test cases. For each test case, it reads an integer `n` and a string `a` from the user input. The function then checks the string `a` for the number of occurrences of the character '1'. It prints 'YES' if the count of '1's is 0, greater than 2 and even, or exactly 2 with a specific spacing condition. Otherwise, it prints 'NO'. The function processes `t` test cases and prints the result for each one. The state of `start` and `end` (if they exist) remains unchanged, as they are not used within the function.


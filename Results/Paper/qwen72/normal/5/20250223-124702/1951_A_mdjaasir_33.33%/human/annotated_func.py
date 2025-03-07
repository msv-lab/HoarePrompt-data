#State of the program right berfore the function call: start and end are integers, and start <= end.
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
        
    #State: The values of `start` and `end` remain unchanged, and `t` remains the same as the initial input integer. The loop does not modify these variables.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any values. It reads an integer `t` from user input, which represents the number of test cases. For each test case, it reads another integer `n` and a string `a` from user input. The function then checks the count of '1' characters in the string `a` and prints 'YES' or 'NO' based on the following conditions: if the count is 0, or greater than 2 and even, or exactly 2 with the two '1's not adjacent, it prints 'YES'; otherwise, it prints 'NO'. The variables `start` and `end` mentioned in the comments are not used in the function.


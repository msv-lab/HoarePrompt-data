#State of the program right berfore the function call: start and end are integers such that 0 <= start <= end, and the current directory contains subfolders with names that are digits.
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
        
    #State: The variables `start` and `end` remain unchanged. The loop iterates `t` times, and during each iteration, it reads an integer `n` and a string `a` from the input. It then prints 'YES' or 'NO' based on the conditions specified in the loop. After `t` iterations, the loop completes, and no further changes are made to any variables.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, indicating the number of test cases. For each test case, it reads an integer `n` and a string `a` from the input. It then checks the number of '1's in the string `a` and prints 'YES' or 'NO' based on the following conditions: if there are no '1's, it prints 'YES'; if there are more than 2 '1's and the count is even, it prints 'YES'; if there are exactly 2 '1's and they are not adjacent, it prints 'YES'; otherwise, it prints 'NO'. After processing all `t` test cases, the function completes without making any changes to external variables or the directory structure.


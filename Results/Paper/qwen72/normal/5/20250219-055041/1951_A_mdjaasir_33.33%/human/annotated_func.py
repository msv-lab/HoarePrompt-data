#State of the program right berfore the function call: start and end are integers where start <= end, and the current directory contains subfolders with names that can be interpreted as integers within the range [start, end].
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
        
    #State: `start` and `end` are integers where `start` <= `end`, the current directory contains subfolders with names that can be interpreted as integers within the range [start, end], `t` is greater than or equal to the number of iterations the loop has executed, `i` is `t - 1`, `n` is the last input integer, `a` is the last input string, and `count` is the number of times the character '1' appears in the last `a`. If `count` is 0, the state remains unchanged. If `count` is greater than 2 and even, the state remains unchanged. If `count` is 2 and the first occurrence of '1' in `a` is followed by another '1', the state also remains unchanged. If `count` is not 2 or does not meet the condition of being followed by another '1', the state remains unchanged.
#Overall this is what the function does:The function reads an integer `t` from the user, and for each of the `t` iterations, it reads another integer `n` and a string `a` from the user. It then checks the number of occurrences of the character '1' in the string `a`. If the count of '1' is 0, or greater than 2 and even, or exactly 2 with the first '1' not followed by another '1', it prints 'YES'. Otherwise, it prints 'NO'. The function does not return any value or modify the state of the program beyond the scope of its execution.


#State of the program right berfore the function call: start and end are integers such that 0 <= start <= end, and the current directory contains subfolders with names that can be interpreted as integers.
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
        
    #State: The values of `start` and `end` remain unchanged, and the current directory still contains the same subfolders with names that can be interpreted as integers. The loop has executed `t` times, and for each iteration, it has read an integer `n` and a string `a` from the input. Depending on the number of '1's in `a`, it has printed 'YES' or 'NO' to the console. After `t` iterations, the loop has finished executing.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, and for each of the `t` iterations, it reads another integer `n` and a string `a`. It then checks the number of '1's in the string `a` and prints 'YES' or 'NO' to the console based on the following conditions: if there are no '1's, it prints 'YES'; if there are more than 2 '1's and the count is even, it prints 'YES'; if there are exactly 2 '1's and they are not consecutive, it prints 'YES'; otherwise, it prints 'NO'. After `t` iterations, the function completes and the state of the program remains unchanged with respect to the `start` and `end` variables and the subfolders in the current directory.


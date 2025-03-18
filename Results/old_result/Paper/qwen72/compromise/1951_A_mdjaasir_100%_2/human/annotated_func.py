#State of the program right berfore the function call: start and end are integers, with start <= end, and the current directory contains subfolders named with digits within the range [start, end]. Each of these subfolders may contain .html files.
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
        
    #State: The values of `start`, `end`, and `t` remain unchanged. The loop has executed `t` times, and for each iteration, it has read an integer `n` and a string `a` from the input. Based on the conditions in the loop, it has printed 'YES' or 'NO' to the console for each iteration. The subfolders and .html files in the current directory are not affected by the loop.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, and for each of the `t` iterations, it reads another integer `n` and a string `a`. It then checks the count of '1' characters in the string `a` and prints 'YES' or 'NO' to the console based on specific conditions: 'YES' if the count is 0, greater than 2 and even, or exactly 2 with the two '1's not adjacent; otherwise, it prints 'NO'. The function does not modify the values of `start`, `end`, or any files in the current directory.


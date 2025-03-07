#State of the program right berfore the function call: start and end are integers such that start <= end, and the current directory contains subfolders with numeric names.
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
        
    #State: The values of `start` and `end` remain unchanged. The variable `t` is decremented by the number of iterations the loop has executed, but since `t` is the loop control variable, it will be 0 after the loop finishes. The subfolders in the current directory remain unchanged.
#Overall this is what the function does:The function reads an integer `t` from the user, and for each of the `t` test cases, it reads an integer `n` and a string `a` from the user. It then checks the number of '1's in the string `a` and prints 'YES' if the count is 0, greater than 2 and even, or exactly 2 with the two '1's not adjacent. Otherwise, it prints 'NO'. The function does not modify the `start` and `end` variables or the subfolders in the current directory.


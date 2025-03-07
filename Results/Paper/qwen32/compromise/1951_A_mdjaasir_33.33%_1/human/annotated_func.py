#State of the program right berfore the function call: start and end are integers such that start <= end.
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
        
    #State: The values of `start` and `end` remain unchanged. The variable `t` remains unchanged. The variables `n`, `a`, and `count` do not retain any specific value after the loop as they are reinitialized in each iteration. The loop prints 'YES' or 'NO' based on the conditions specified for each iteration, but these print statements do not affect the state of `start`, `end`, or `t`.
#Overall this is what the function does:The function reads an integer `t` from the input, then for each of the next `t` iterations, it reads another integer `n` and a string `a`. It counts the number of '1's in the string `a` and prints 'YES' if the count is 0, if the count is greater than 2 and even, or if the count is exactly 2 and the two '1's are not adjacent. Otherwise, it prints 'NO'. The function does not return any value; it only prints to the console. The parameters `start` and `end` mentioned in the annotations are not used within the function.


#State of the program right berfore the function call: start and end are integers such that 0 <= start <= end, and the current directory contains subfolders with names that can be converted to integers within the range [start, end], and these subfolders may contain .html files.
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        cnt1 = s.count('1')
        
        if cnt1 > 2 and cnt1 % 2 == 0:
            print('YES')
        elif cnt1 > 2 and (cnt1 % 2 == 1 or cnt1 == 1):
            print('NO')
        elif '11' in s:
            print('NO')
        else:
            print('YES')
        
    #State: The values of `start`, `end`, and the current directory contents remain unchanged. The loop iterates `t` times, processing input values `n` and `s` each time, and prints 'YES' or 'NO' based on the conditions specified in the loop.
#Overall this is what the function does:The function `func_1` processes a series of inputs, where the first input `t` specifies the number of test cases. For each test case, it reads an integer `n` and a string `s`, then prints 'YES' or 'NO' based on the conditions: if the count of '1' in `s` is greater than 2 and even, it prints 'YES'; if the count is greater than 2 and odd or exactly 1, it prints 'NO'; if the string '11' is present in `s`, it prints 'NO'; otherwise, it prints 'YES'. The function does not modify the values of `start`, `end`, or the current directory contents.


#State of the program right berfore the function call: start and end are integers such that start <= end, and the current working directory contains subfolders named with digits within the range [start, end].
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
        
    #State: The values of `start`, `end`, and the current working directory remain unchanged. The loop has executed `t` times, and for each iteration, it has taken an integer `n` and a string `s` as input, processed them according to the conditions, and printed either 'YES' or 'NO' based on the conditions. The final output state is the same as the initial state, except that the loop has completed its `t` iterations.
#Overall this is what the function does:The function `func_1` accepts no parameters and does not return any value. It reads an integer `t` from the user, which specifies the number of test cases. For each test case, it reads an integer `n` and a string `s` from the user. The function then checks the string `s` for the presence of the character '1' and prints 'YES' or 'NO' based on the following conditions: if the count of '1' is greater than 2 and even, it prints 'YES'; if the count of '1' is greater than 2 and odd, or exactly 1, it prints 'NO'; if the substring '11' is present in `s`, it prints 'NO'; otherwise, it prints 'YES'. The function does not modify the values of `start`, `end`, or the current working directory. After executing `t` test cases, the function completes and the program state remains unchanged except for the printed outputs.


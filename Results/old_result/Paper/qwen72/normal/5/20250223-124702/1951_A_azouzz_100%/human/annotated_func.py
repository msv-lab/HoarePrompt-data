#State of the program right berfore the function call: start and end are integers where start <= end, and they represent the range of folder names to be considered, which are expected to be numeric.
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        cnt1 = s.count('1')
        
        if cnt1 > 2 and cnt1 % 2 == 0:
            print('YES')
        elif cnt1 > 2:
            print('NO')
        elif cnt1 == 1:
            print('NO')
        elif '11' in s:
            print('NO')
        else:
            print('YES')
        
    #State: The values of `start`, `end`, and `t` remain unchanged. The loop prints 'YES' or 'NO' for each iteration based on the conditions provided in the loop body.
#Overall this is what the function does:The function `func_1` does not accept any parameters and does not return any value. It reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads another integer `n` and a string `s` from the input. The function then checks the string `s` for the following conditions: if the count of '1' characters is greater than 2 and even, it prints 'YES'; if the count is greater than 2 but odd, it prints 'NO'; if the count is exactly 1, it prints 'NO'; if the string contains the substring '11', it prints 'NO'; otherwise, it prints 'YES'. The values of `start` and `end` mentioned in the comments are not used or modified by the function.


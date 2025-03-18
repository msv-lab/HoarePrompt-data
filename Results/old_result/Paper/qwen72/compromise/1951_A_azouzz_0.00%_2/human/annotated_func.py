#State of the program right berfore the function call: start and end are integers such that 0 <= start <= end.
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
        
    #State: The values of `start` and `end` remain unchanged, and `t` is decremented by the number of iterations that the loop has executed. The loop itself does not modify any of these variables.
#Overall this is what the function does:The function `func_1` does not accept any parameters and does not return any value. It reads an integer `t` from the user, which represents the number of test cases. For each test case, it reads another integer `n` and a string `s` of length `n`. The function checks the string `s` for the following conditions: if the count of '1' characters is greater than 2 and even, it prints 'YES'; if the count is greater than 2 and odd, or exactly 1, it prints 'NO'; if the string contains the substring '11', it prints 'NO'; otherwise, it prints 'YES'. The function does not modify any external variables or state.


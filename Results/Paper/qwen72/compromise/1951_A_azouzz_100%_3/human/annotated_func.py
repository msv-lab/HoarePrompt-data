#State of the program right berfore the function call: start and end are integers such that 0 <= start <= end.
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
        
    #State: The values of `start`, `end`, and `t` remain unchanged. The loop has executed `t` times, and for each iteration, it has read an integer `n` and a string `s` from the input, then printed 'YES' or 'NO' based on the conditions provided in the loop.
#Overall this is what the function does:The function `func_1` does not accept any parameters and does not return any values. It reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads an integer `n` and a string `s` from the input. The function then checks the string `s` for specific conditions related to the count of '1' characters and the presence of the substring '11'. Based on these conditions, it prints 'YES' or 'NO' for each test case. The values of `start` and `end` (if they exist in the calling context) remain unchanged.


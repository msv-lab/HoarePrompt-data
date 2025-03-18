#State of the program right berfore the function call: start and end are integers such that start <= end, and they represent the range of folder names to be considered, where folder names are numeric.
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
        
    #State: `start` and `end` remain unchanged, `t` is 0.
#Overall this is what the function does:The function `func_1` does not accept any parameters and does not return any values. It reads an integer `t` from the input, representing the number of test cases. For each test case, it reads another integer `n` and a string `s` from the input. The function then checks the string `s` for the number of occurrences of the character '1'. If the count of '1' is greater than 2 and even, it prints 'YES'. If the count is greater than 2 but odd, it prints 'NO'. If the count is exactly 1, it prints 'NO'. If the string contains the substring '11', it prints 'NO'. Otherwise, it prints 'YES'. After processing all test cases, the function concludes, and the variables `start` and `end` (if they exist) remain unchanged.


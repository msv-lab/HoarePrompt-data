#State of the program right berfore the function call: start and end are integers such that 0 <= start <= end.
def func():
    t = int(input())
    while t > 0:
        n = int(input())
        
        s = input()
        
        if n == 2:
            if s == '00':
                print('YES')
            else:
                print('NO')
        else:
            count_1 = s.count('1')
            if count_1 % 2 != 0:
                print('NO')
            elif s.count('11') == 1:
                print('NO')
            else:
                print('YES')
        
        t -= 1
        
    #State: `t` is 0, `start` and `end` remain unchanged.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any values. It reads an integer `t` from the user, representing the number of test cases. For each test case, it reads another integer `n` and a string `s` from the user. The function then checks if the string `s` meets certain conditions based on the value of `n`. If `n` is 2 and `s` is '00', it prints 'YES'. Otherwise, if the count of '1' in `s` is odd or if the substring '11' appears exactly once, it prints 'NO'. In all other cases, it prints 'YES'. After processing all test cases, the value of `t` is 0, and any external variables like `start` and `end` remain unchanged.


#State of the program right berfore the function call: start and end are integers, and start <= end.
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
        
    #State: `t` is 0, and the values of `start` and `end` remain unchanged.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any values. It reads an integer `t` from the user, which represents the number of test cases. For each test case, it reads another integer `n` and a string `s` from the user. The function then checks if the string `s` meets certain conditions based on the value of `n`. If `n` is 2, it prints 'YES' if `s` is '00', otherwise it prints 'NO'. For `n` greater than 2, it prints 'NO' if the count of '1' in `s` is odd or if the substring '11' appears exactly once; otherwise, it prints 'YES'. After processing all test cases, the function concludes with `t` being 0, and any external variables `start` and `end` (if they exist) remain unchanged.


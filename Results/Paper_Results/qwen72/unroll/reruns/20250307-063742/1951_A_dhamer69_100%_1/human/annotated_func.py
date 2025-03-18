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
            elif s.count('11') == 1 and count_1 == 2:
                print('NO')
            else:
                print('YES')
        
        t -= 1
        
    #State: `t` is 0, and the loop has finished executing. The values of `start` and `end` remain unchanged.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any values. It reads an integer `t` from the user, representing the number of test cases. For each test case, it reads another integer `n` and a string `s` from the user. The function then checks if the string `s` meets certain conditions based on the value of `n` and prints 'YES' or 'NO' accordingly. After processing all test cases, the function concludes with `t` being 0. The function does not modify any external variables or parameters.


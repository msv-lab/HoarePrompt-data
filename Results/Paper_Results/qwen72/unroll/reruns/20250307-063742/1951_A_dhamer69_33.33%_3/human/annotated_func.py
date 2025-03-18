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
        
    #State: `t = 0`
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any values. It reads an integer `t` from the user input, representing the number of test cases. For each test case, it reads another integer `n` and a string `s` from the user input. The function checks if the string `s` meets certain conditions based on the value of `n` and prints 'YES' or 'NO' accordingly. After processing all test cases, the variable `t` is set to 0.


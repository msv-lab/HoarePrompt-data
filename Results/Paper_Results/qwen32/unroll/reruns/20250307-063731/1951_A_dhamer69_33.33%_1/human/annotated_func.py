#State of the program right berfore the function call: start and end are integers such that start <= end.
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
        
    #State: t = 0, start and end remain unchanged.
#Overall this is what the function does:The function reads multiple test cases from the input. For each test case, it reads an integer `n` and a string `s` of length `n`. It then determines whether the string `s` meets certain conditions based on the number of '1's in the string and the presence of consecutive '1's. Specifically, if `n` is 2, it checks if the string is '00'. For other values of `n`, it checks if the number of '1's is even and not all '1's are consecutive. It prints 'YES' if the conditions are met and 'NO' otherwise. The function does not return any value; it outputs the results directly.


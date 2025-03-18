#State of the program right berfore the function call: start and end are non-negative integers such that start <= end.
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
        
    #State: t = 0.
#Overall this is what the function does:The function reads multiple test cases from the input. For each test case, it checks a string `s` of length `n`. If `n` is 2, it prints 'YES' only if `s` is '00'; otherwise, it prints 'NO'. For `n` greater than 2, it prints 'YES' if the count of '1's in `s` is even and there is not exactly one occurrence of '11'; otherwise, it prints 'NO'.


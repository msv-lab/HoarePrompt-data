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
            elif s.count('11') == 1 and count_1 == 2:
                print('NO')
            else:
                print('YES')
        
        t -= 1
        
    #State: `start` and `end` are integers such that `start` <= `end`; `t` is 0.
#Overall this is what the function does:The function reads an integer `t` and then processes `t` test cases. For each test case, it reads an integer `n` and a string `s` of length `n`. It prints 'YES' if the string `s` meets certain conditions related to the number of '1's in the string, and 'NO' otherwise. The conditions are: if `n` is 2, `s` must be '00' to print 'YES'. For `n` greater than 2, the number of '1's in `s` must be even, and if there is exactly one '11' and the total number of '1's is 2, it prints 'NO'.


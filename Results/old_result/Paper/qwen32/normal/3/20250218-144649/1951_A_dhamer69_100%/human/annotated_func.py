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
            elif s.count('11') == 1 and count_1 == 2:
                print('NO')
            else:
                print('YES')
        
        t -= 1
        
    #State: `start` and `end` are non-negative integers such that `start` <= `end`; `t` is 0.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads an integer `n` and a string `s` of length `n`. It then checks specific conditions based on the value of `n` and the content of `s` to determine if it should print 'YES' or 'NO'. If `n` is 2, it prints 'YES' only if `s` is '00'. Otherwise, it prints 'YES' if the number of '1's in `s` is even and not both conditions `count_1 == 2` and `s.count('11') == 1` are satisfied; otherwise, it prints 'NO'. The function repeats this process `t` times.


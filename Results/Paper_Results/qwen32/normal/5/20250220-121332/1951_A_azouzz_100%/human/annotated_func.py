#State of the program right berfore the function call: start and end are non-negative integers such that start <= end.
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
        
    #State: `start` and `end` are non-negative integers such that `start` <= `end`; `t` is 0; no further iterations occur; `n` and `s` are undefined as they are not retained after the loop ends; `cnt1` is undefined as it is not retained after the loop ends.
#Overall this is what the function does:The function `func_1` reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a string `s`. It then determines if the number of '1's in the string `s` meets certain conditions and prints 'YES' or 'NO' based on those conditions. The final state of the program is that it has processed all test cases and printed the corresponding 'YES' or 'NO' for each.


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
        
    #State: start and end are integers such that start <= end; t is 0; no changes are made to start, end, or t regardless of the values of n or s in the loop body.
#Overall this is what the function does:The function reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `n` and a string `s` of length `n`. Based on the value of `n` and the contents of `s`, it prints 'YES' or 'NO' according to specific conditions. The function does not modify or return the input parameters `start` and `end` as mentioned in the annotations, and it does not return any value itself.


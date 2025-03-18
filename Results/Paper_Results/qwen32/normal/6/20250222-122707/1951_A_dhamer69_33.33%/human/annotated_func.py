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
        
    #State: `start` and `end` are integers such that `start` <= `end`; `t` is 0; no further iterations of the loop will occur.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a string `s` of length `n`. It then prints 'YES' or 'NO' based on specific conditions related to the count of '1's in the string `s`. The function does not return any value; it only prints output for each test case.


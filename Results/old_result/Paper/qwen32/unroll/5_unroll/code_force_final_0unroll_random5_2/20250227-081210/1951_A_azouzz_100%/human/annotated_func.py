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
        
    #State: start and end are non-negative integers such that start <= end; t is an input integer.
#Overall this is what the function does:The function `func_1` reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a string `s`. It then determines if the string `s` meets specific conditions related to the count of '1's in the string and prints 'YES' or 'NO' based on these conditions. The function does not accept parameters `start` and `end` as described in the annotations, and it does not return any value; instead, it outputs strings to the console.


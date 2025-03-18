#State of the program right berfore the function call: start and end are integers such that start <= end, and both start and end are used to filter folder names which should be digits within the specified range.
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        cnt1 = s.count('1')
        
        if cnt1 > 2 and cnt1 % 2 == 0:
            print('YES')
        elif cnt1 > 2 and (cnt1 % 2 == 1 or cnt1 == 1):
            print('NO')
        elif '11' in s:
            print('NO')
        else:
            print('YES')
        
    #State: `t` is a positive integer minus the total number of iterations, `start` is an integer, `end` is an integer such that `start` <= `end`, `n` is the integer input by the user for the last iteration, `s` is the new input string from the user for the last iteration, `cnt1` is the count of '1' in the string `s` for the last iteration. If `cnt1` > 2 and `cnt1` is even, no changes are made to the variables. If `cnt1` > 2 and `cnt1` is odd or `cnt1` == 1, no changes are made to the variables. If `'11'` is found in `s`, no changes are made to the variables. If none of the above conditions are met, no changes are made to the variables.
#Overall this is what the function does:The function processes multiple inputs, each consisting of an integer `n` followed by a string `s`. It checks the string `s` for specific conditions related to the count of '1' characters and the presence of '11'. Based on these conditions, it prints either 'YES' or 'NO'. The function does not modify any external variables and does not accept any parameters.


#State of the program right berfore the function call: start and end are integers such that start <= end.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        a = input()
        
        count = a.count('1')
        
        if count == 0:
            print('YES')
        elif count > 2 and count % 2 == 0:
            print('YES')
        elif count == 2:
            if a.index('1') and a[a.index('1') + 1] != '1':
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
        
    #State: `start` and `end` are integers such that `start <= end`, `t` is an integer representing the number of iterations, `i` is equal to `t`, `n` is the integer input from the last iteration, `a` is the string input from the last iteration, and `count` is the number of '1's in the string `a` from the last iteration.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a string `a`. It then determines if the number of '1's in the string `a` meets specific conditions and prints 'YES' or 'NO' based on these conditions. The function does not return any value explicitly; it outputs 'YES' or 'NO' for each test case.


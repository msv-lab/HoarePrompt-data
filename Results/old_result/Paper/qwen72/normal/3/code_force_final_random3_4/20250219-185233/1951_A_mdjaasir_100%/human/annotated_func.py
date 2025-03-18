#State of the program right berfore the function call: start and end are integers where 0 <= start <= end, and the current working directory contains subfolders with names that can be interpreted as integers.
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
            if a[a.index('1') + 1] != '1':
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
        
    #State: `t` is greater than or equal to the number of iterations, `i` is `t-1`, `n` is an input integer, `a` is the last input string, and `count` is the number of times '1' appears in `a`. If `count` is 0, greater than 2 and even, 2 and the character following the first '1' in `a` is not '1', 2 and the character following the first '1' in `a` is '1', or not 2 or not even, the postcondition remains unchanged.
#Overall this is what the function does:The function reads an integer `t` from the user, indicating the number of test cases. For each test case, it reads an integer `n` and a string `a` from the user. It then checks the number of '1's in the string `a` and prints 'YES' or 'NO' based on specific conditions: it prints 'YES' if there are no '1's, if there are more than 2 '1's and the count is even, or if there are exactly 2 '1's and they are not consecutive. Otherwise, it prints 'NO'. After processing all test cases, the function completes without returning any value.


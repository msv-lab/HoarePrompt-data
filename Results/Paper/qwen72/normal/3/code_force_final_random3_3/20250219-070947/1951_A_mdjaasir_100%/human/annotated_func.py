#State of the program right berfore the function call: start and end are integers such that start <= end, and they define the range of folder names to be considered, where folder names are expected to be numeric.
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
        
    #State: `start` and `end` are integers such that `start` <= `end`, `t` is an input integer, `i` is `t-1`, `n` is an input integer, `a` is an input string, and `count` is the number of occurrences of '1' in `a`. If `count` is 0, the program prints 'YES'. If `count` is greater than 2 and even, or if `count` is exactly 2 and the first '1' in `a` is not immediately followed by another '1', the program prints 'YES'. Otherwise, if `count` is exactly 2 and the second '1' in `a` is immediately after the first '1', or if `count` is greater than 0 and either less than or equal to 2 or odd but not equal to 2, the program prints 'NO'.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any values. It reads an integer `t` from the user input, which represents the number of test cases. For each test case, it reads another integer `n` and a string `a` from the user input. The function then counts the number of occurrences of '1' in the string `a`. If the count is 0, greater than 2 and even, or exactly 2 with the first '1' not immediately followed by another '1', it prints 'YES'. Otherwise, it prints 'NO'. After processing all test cases, the function concludes.


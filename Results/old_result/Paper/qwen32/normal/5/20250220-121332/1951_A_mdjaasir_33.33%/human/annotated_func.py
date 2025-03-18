#State of the program right berfore the function call: start and end are non-negative integers such that start <= end.
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
        
    #State: `start` and `end` are non-negative integers such that `start` <= `end`; `t` is greater than 0; `i` is equal to `t`; `n` is the last input integer; `a` is the last string input by the user; `count` is the number of '1's in the last string `a`. The program has printed 'YES' or 'NO' for each of the `t` iterations based on the conditions specified.
#Overall this is what the function does:The function reads an integer `t` from the input, representing the number of test cases. For each test case, it reads another integer `n` and a string `a`. It then counts the number of '1's in the string `a` and prints 'YES' if the count is 0, greater than 2 and even, or exactly 2 with the '1's not adjacent; otherwise, it prints 'NO'. The function does not return any value; it only prints the results for each test case.


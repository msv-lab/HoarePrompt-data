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
            if a[a.index('1') + 1] != '1':
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
        
    #State: `start` and `end` are integers such that `start <= end`; `t` is greater than 0; `i` is `t-1`; `n` is the integer input by the user in the last iteration; `a` is the string input by the user in the last iteration; `count` is the number of '1's in `a`. The loop has finished executing all `t` iterations.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads another integer `n` and a string `a`. It then counts the number of '1's in the string `a` and prints 'YES' if the count is 0, if the count is greater than 2 and even, or if the count is exactly 2 and the two '1's are not adjacent. Otherwise, it prints 'NO'. The function does not return any value; it only prints the results for each test case.


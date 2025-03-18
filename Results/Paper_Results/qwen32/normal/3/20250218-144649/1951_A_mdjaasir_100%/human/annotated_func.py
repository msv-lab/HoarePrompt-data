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
            if a[a.index('1') + 1] != '1':
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
        
    #State: `start` and `end` are non-negative integers such that `start` <= `end`, `t` is a positive integer, `i` is equal to `t`, `n` is the integer input from the last iteration, `a` is the string input from the last iteration, and `count` is the number of '1's in the last string input.
#Overall this is what the function does:The function reads an integer `t`, then for each of the next `t` test cases, it reads an integer `n` and a string `a`. It counts the number of '1's in the string `a` and prints 'YES' if the count is 0, or if the count is greater than 2 and even, or if the count is exactly 2 and the two '1's are not adjacent. Otherwise, it prints 'NO'.


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
        
    #State: start and end are integers such that start <= end; t is an input integer.
#Overall this is what the function does:The function reads an integer `t` and then processes `t` test cases. For each test case, it reads an integer `n` and a string `a`. It counts the number of '1's in the string `a` and prints 'YES' if the count is 0, greater than 2 and even, or exactly 2 with the two '1's not adjacent. Otherwise, it prints 'NO'.


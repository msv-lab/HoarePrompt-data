#State of the program right berfore the function call: start and end are integers such that start <= end, and both start and end represent valid directory names in the current working directory (os.getcwd()).
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
        
    #State: Output State: The output state will consist of a series of 'YES' and 'NO' responses based on the conditions evaluated within the loop for each iteration of `i` from `0` to `t-1`. For each iteration, the value of `n` and the string `a` are read from input, and the program checks the number of '1's in `a`. If there are no '1's, it prints 'YES'. If there are more than 2 '1's and their count is even, it also prints 'YES'. If there are exactly 2 '1's, it checks if the second '1' is not immediately following the first '1'; if so, it prints 'YES', otherwise it prints 'NO'. For all other cases, it prints 'NO'.
#Overall this is what the function does:The function reads multiple test cases from standard input. For each test case, it reads an integer `n` and a binary string `a`. It then checks the number of '1's in the string `a`. Based on the count of '1's, it prints 'YES' or 'NO' to the standard output. Specifically, it prints 'YES' if there are no '1's, more than two '1's with an even count, or exactly two '1's that are not adjacent. Otherwise, it prints 'NO'.


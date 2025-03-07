#State of the program right berfore the function call: start and end are integers such that start <= end, and both represent valid directory names without leading zeros.
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
        
    #State: Output State: The output state will consist of "YES" or "NO" printed for each iteration of the loop based on the conditions provided in the loop body. Specifically, for each value of `n` (read from input) and string `a` (also read from input), the program checks the number of '1's in `a`. If the count is 0, it prints 'YES'. If the count is greater than 2 and even, it prints 'YES'. If the count is exactly 2, it checks if the second '1' is not immediately following the first '1'; if so, it prints 'YES', otherwise it prints 'NO'. For all other cases, it prints 'NO'. The final output state will be a series of "YES" or "NO" responses corresponding to each input pair `(n, a)` within the loop.
#Overall this is what the function does:The function reads multiple pairs of inputs, where each pair consists of an integer `n` and a binary string `a`. It then checks the number of '1's in the string `a`. Based on the count of '1's, it prints either 'YES' or 'NO' for each pair. Specifically, if the count is 0, it prints 'YES'. If the count is greater than 2 and even, it also prints 'YES'. If the count is exactly 2, it checks if the second '1' is not immediately following the first '1'; if so, it prints 'YES', otherwise it prints 'NO'. For all other cases, it prints 'NO'. After processing all input pairs, the function concludes with a series of 'YES' or 'NO' responses corresponding to each input pair.


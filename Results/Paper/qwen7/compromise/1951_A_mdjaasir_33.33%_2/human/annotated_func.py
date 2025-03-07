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
            if a.index('1') and a[a.index('1') + 1] != '1':
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
        
    #State: Output State: The output state will consist of "YES" or "NO" printed for each iteration of the loop based on the conditions specified within the loop body. Specifically, for each value of `n` (input) and string `a` (input), the loop checks the number of '1's in `a`. If the count is 0, it prints 'YES'. If the count is greater than 2 and even, it prints 'YES'. If the count is exactly 2, it checks if there is exactly one '1' with no adjacent '1's; if so, it prints 'YES', otherwise 'NO'. For all other cases, it prints 'NO'.
    #
    #Each iteration's output depends solely on the inputs `n` and `a` for that particular iteration, and these outputs are printed sequentially during the loop execution.
#Overall this is what the function does:The function processes multiple inputs, each consisting of an integer `n` followed by a binary string `a`. It checks the number of '1's in the string `a` and prints 'YES' or 'NO' based on specific conditions. If the count of '1's is 0, it prints 'YES'. If the count is greater than 2 and even, it prints 'YES'. If the count is exactly 2, it checks if there is exactly one '1' with no adjacent '1's; if so, it prints 'YES', otherwise 'NO'. For all other cases, it prints 'NO'. The function does not return any value but prints the results for each input.


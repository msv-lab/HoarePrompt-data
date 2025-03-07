#State of the program right berfore the function call: start and end are integers such that start <= end, and both represent valid directory names in the current working directory.
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
        
    #State: Output State: The output state will consist of a series of 'YES' and 'NO' responses based on the conditions evaluated for each iteration of the loop. For each iteration, the value of `n` (obtained from `input()`) and the string `a` (also obtained from `input()`) are used to determine whether the condition `count == 0`, `count > 2 and count % 2 == 0`, or `count == 2` with additional checks is met. If any of these conditions are true, 'YES' is printed; otherwise, 'NO' is printed. The final output state will be a list of these 'YES' and 'NO' responses, one for each iteration of the loop.
#Overall this is what the function does:The function reads multiple inputs from the user, including an integer `t`, followed by `t` pairs of an integer `n` and a binary string `a`. It then checks the number of '1's in each binary string `a`. Based on the count of '1's, it prints 'YES' or 'NO' for each pair. Specifically, it prints 'YES' if the count is 0, greater than 2 and even, or exactly 2 with the second '1' not immediately following the first '1'; otherwise, it prints 'NO'. The function does not return anything but outputs a series of 'YES' and 'NO' responses.


#State of the program right berfore the function call: start and end are integers such that start <= end, and both start and end represent valid folder names in the current directory, where folder names are digits.
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
        
    #State: Output State: The output state will consist of a series of 'YES' and 'NO' responses based on the conditions evaluated for each iteration of the loop. For each iteration, the value of `n` (obtained from `input()`) and the string `a` (also obtained from `input()`) are processed to determine if the number of '1's in `a` meets certain criteria, and then either 'YES' or 'NO' is printed accordingly. The final output state will be a list of these printed results, one for each iteration of the loop.
#Overall this is what the function does:The function reads multiple inputs from the user, processes each input to count the occurrences of '1' in a given string, and prints 'YES' or 'NO' based on specific conditions related to the count. The function does not return any value; instead, it outputs a series of 'YES' and 'NO' responses.


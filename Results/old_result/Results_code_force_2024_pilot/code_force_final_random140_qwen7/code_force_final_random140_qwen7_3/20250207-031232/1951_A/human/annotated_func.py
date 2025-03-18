#State of the program right berfore the function call: start and end are integers such that start <= end, and both represent valid directory names without leading zeros.
def func():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        
        arr = input()
        
        count_ones = arr.count('1')
        
        if count_ones == 0:
            results.append('yes')
        elif count_ones % 2 != 0:
            results.append('no')
        elif count_ones == 2:
            if '11' in arr:
                results.append('no')
            else:
                results.append('yes')
        else:
            results.append('yes')
        
    #State: Output State: `start` is an integer, `end` is an integer, `t` is 0, `results` is a list containing 'yes' and 'no', `n` is the integer input from the user, `arr` is the string input from the user, `count_ones` is the count of '1's in `arr`.
    #
    #Explanation: After the loop has executed all its iterations (i.e., `t` becomes 0), the loop condition `_ in range(t)` fails, meaning no further iterations will occur. The value of `t` is set to 0 at the start of each iteration, so it will remain 0 after all iterations. The `results` list accumulates answers based on the conditions checked within the loop, but since `t` is now 0, no new elements will be appended to `results`. Therefore, `results` retains whatever values were added during the previous iterations, which in this case is described as a list containing 'yes' and 'no'.
    for r in results:
        print(r)
        
    #State: `results` is a list containing 'yes' and 'no'.
#Overall this is what the function does:The function reads multiple test cases, where each test case consists of an integer `n` and a binary string `arr`. It checks the number of '1's in `arr` and appends 'yes' or 'no' to the `results` list based on specific conditions. Finally, it prints the contents of the `results` list. The function does not accept any parameters and does not return anything.


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
        
    #State: Output State: The `results` list will contain 'yes' or 'no' based on the conditions evaluated for each input string `arr` over all iterations. For each iteration, `n` (an integer) and `arr` (a string) are read from input. The variable `count_ones` counts the number of '1's in `arr`. If `count_ones` is 0, 'yes' is appended to `results`. If `count_ones` is odd, 'no' is appended. If `count_ones` is exactly 2, 'no' is appended if '11' is in `arr`, otherwise 'yes' is appended. For any other even `count_ones`, 'yes' is appended if '11' is not in `arr`, otherwise 'no' is appended. After all iterations, `results` will contain the outcomes for each input string `arr` according to the specified conditions.
    for r in results:
        print(r)
        
    #State: The `results` list will contain all the outcomes for each input string `arr` based on the specified conditions after all iterations of the loop have finished.
#Overall this is what the function does:The function reads multiple inputs consisting of integers and strings. For each input string, it counts the number of '1's. Based on the count and the presence of '11' in the string, it appends either 'yes' or 'no' to a list. After processing all inputs, it prints each element in the list. The function does not return any value.


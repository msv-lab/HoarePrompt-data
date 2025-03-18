#State of the program right berfore the function call: arr is a list of integers where the length of the list is n (1 <= n <= 2 * 10^5), and each element a_i satisfies 1 <= a_i <= n.
def func_1(arr):
    i = 0
    j = len(arr) - 1
    while i <= j:
        if arr[i] == arr[j]:
            i += 1
            j -= 1
        else:
            break
        
    #State: Output State: `i` is greater than or equal to `j`.
    #
    #This means that after the loop has executed all its iterations, the variable `i` will be greater than or equal to the variable `j`. This is because the loop continues as long as `i` is less than or equal to `j`. Once `i` becomes greater than `j`, the condition `i <= j` in the while loop head fails, and the loop terminates. At this point, the array has been checked for matching elements from both ends towards the center, and the loop naturally stops when there are no more pairs to compare or when a mismatch is found.
    if (i > j) :
        return 0
        #The program returns 0
    #State: `i` is greater than or equal to `j`, and `i` is not greater than `j`
    while arr[i] == arr[i + 1]:
        i += 1
        
    #State: The value of `i` is equal to `j` + 4, and the condition `arr[i - 1]` is equal to `arr[i]` holds true.
    if (j != len(arr) - 1) :
        return j - i + 1
        #The program returns a value that is j - i + 1, where i is equal to j + 4 and the condition arr[i - 1] equals arr[i] holds true.
    #State: The value of `i` is equal to `j` + 4, and the condition `arr[i - 1]` is equal to `arr[i]` holds true, and `j` is equal to `len(arr) - 1`
    return j - i
    #The program returns -1
#Overall this is what the function does:The function accepts a list of integers `arr` and returns one of three values based on the conditions met within the list:
- It returns 0 if no valid pair of indices `(i, j)` satisfying specific conditions exists.
- It returns the length of a subarray from index `i` to `j` (inclusive) if a valid pair exists and meets certain criteria.
- It returns -1 if no valid pair is found and the end of the list is reached without meeting the criteria.


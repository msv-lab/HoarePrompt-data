#State of the program right berfore the function call: array is a list of integers representing a permutation of length n, and find is an integer such that 1 <= find <= n.
def func_1(array, find):
    n = len(array)
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        
        if array[mid] >= find:
            r = mid - 1
        else:
            l = mid + 1
        
    #State: Output State: The list `array` remains a permutation of integers of length `n`, `l` is either 0 or the final value it takes after the last iteration, `r` is either `mid - 1` or 0, and `mid` is the final midpoint calculated as `(l + r) // 2`.
    #
    #In simpler terms, after all iterations of the loop have finished, the list `array` stays the same, `l` will be either 0 or the last computed midpoint plus one, `r` will be either the last computed midpoint minus one or 0, and `mid` will be the final midpoint value. The loop terminates when `l` becomes greater than `r`, indicating that the search range has been exhausted without finding an element that meets the condition `array[mid] >= find`.
    if (l != array.index(find)) :
        print(1)
        #This is printed: 1
        return [str(l + 1), str(array.index(find) + 1)]
        #The program returns a list containing two strings: the first string is the index of `l` incremented by 1, and the second string is the index of `find` in the list `array` incremented by 1.
    else :
        print(0)
        #This is printed: 0
    #State: The list `array` remains a permutation of integers of length `n`, `l` will be either 0 or the last computed midpoint plus one, `r` will be either the last computed midpoint minus one or 0, and `mid` will be the final midpoint value. The search range has been exhausted without finding an element that meets the condition `array[mid] >= find`.
#Overall this is what the function does:The function accepts a list of integers `array` representing a permutation of length `n` and an integer `find` such that 1 <= `find` <= `n`. It performs a binary search on `array` to find the index of `find`. If `find` is in `array`, it returns a list containing the index of `find` in `array` incremented by 1 twice. If `find` is not in `array`, it prints `0` and returns a list containing the index of `l` incremented by 1 twice. The list `array` remains unchanged throughout the function's execution.


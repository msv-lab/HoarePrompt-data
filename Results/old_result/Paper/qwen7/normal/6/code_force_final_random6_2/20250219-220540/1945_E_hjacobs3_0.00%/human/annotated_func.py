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
        
    #State: Output State: The final output state after the loop executes all its iterations is as follows: `array` is a list of integers representing a permutation of length n; `l` is either 0 or a value such that there are no elements in the sublist `array[l:r+1]` that are greater than or equal to `find`; `r` is either n-1 or a value such that there are no elements in the sublist `array[l:r+1]` that are less than `find`; `mid` is the last calculated midpoint value during the loop's execution.
    #
    #In simpler terms, after the loop completes all its iterations, `l` and `r` will define a range within the original array where no element is equal to or greater than `find` (if `l > r`), or `l` and `r` will point to the boundaries of the subarray where `find` could potentially reside (if `l <= r`).
    if (l != array.index(find)) :
        print(1)
        #This is printed: 1
        return [str(l + 1), str(array.index(find) + 1)]
        #The program returns a list containing two strings: the first string is the index of `find` in the `array` list converted to a string, and the second string is also the index of `find` in the `array` list converted to a string.
    else :
        print(0)
        #This is printed: 0
    #State: `array` is a list of integers representing a permutation of length n; `l` and `r` define a range within the original array where no element is equal to or greater than `find` (if `l > r`), or `l` and `r` point to the boundaries of the subarray where `find` could potentially reside (if `l <= r`); `mid` is the last calculated midpoint value during the loop's execution. Moreover, `l` is equal to `array.index(find)`.
#Overall this is what the function does:The function accepts a list of integers (`array`) representing a permutation and an integer (`find`) within the range of the list indices. It performs a binary search to locate `find` within `array`. If `find` is found, it returns a list with the index of `find` as both elements. If `find` is not found, it prints `0` and returns a list with the same index as the first element and `-1` as the second element.


#State of the program right berfore the function call: array is a permutation of integers from 1 to n, and find is an integer such that 1 <= find <= n.
def func_1(array, find):
    n = len(array)
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        
        if array[mid] >= find:
            r = mid - 1
        else:
            l = mid + 1
        
    #State: `array` is a permutation of integers from 1 to n, `find` is an integer such that 1 <= `find` <= n, `n` is the length of `array`, `l` is the smallest index such that `array[l]` >= `find`, or `l` is n if no such index exists. `r` is the largest index such that `array[r]` < `find`, or `r` is -1 if no such index exists.
    if (l != array.index(find)) :
        print(1)
        #This is printed: 1
        return [str(l + 1), str(array.index(find) + 1)]
        #The program returns a list containing two strings: the first string is the result of converting `l + 1` to a string, where `l` is the smallest index such that `array[l]` is greater than or equal to `find`, or `n` if no such index exists; the second string is the result of converting the index of `find` in `array` plus 1 to a string.
    else :
        print(0)
        #This is printed: 0
    #State: `array` is a permutation of integers from 1 to n, `find` is an integer such that 1 <= `find` <= n, `n` is the length of `array`, `l` is the smallest index such that `array[l]` >= `find`, or `l` is n if no such index exists. `r` is the largest index such that `array[r]` < `find`, or `r` is -1 if no such index exists. Additionally, `l` is equal to the index of `find` in `array`.
#Overall this is what the function does:The function `func_1` accepts an array (a permutation of integers from 1 to n) and an integer `find` (1 <= find <= n). It returns a list of two strings: the first string is the smallest index plus 1 where the array value is greater than or equal to `find`, or `n` if no such index exists; the second string is the index of `find` in the array plus 1. Additionally, the function prints `1` if the smallest index `l` such that `array[l]` is greater than or equal to `find` is not the same as the index of `find` in the array, and `0` otherwise.


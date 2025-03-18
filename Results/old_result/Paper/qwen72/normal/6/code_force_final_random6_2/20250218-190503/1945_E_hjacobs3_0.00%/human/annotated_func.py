#State of the program right berfore the function call: array is a list of integers representing a permutation of size n where 1 <= n <= 2 * 10^5, and all elements in array are distinct integers from 1 to n. find is an integer such that 1 <= find <= n.
def func_1(array, find):
    n = len(array)
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        
        if array[mid] >= find:
            r = mid - 1
        else:
            l = mid + 1
        
    #State: `n` is equal to the length of the `array`, `array` is a list of integers representing a permutation of size `n` where 1 <= `n` <= 2 * 10^5, and all elements in `array` are distinct integers from 1 to `n`. `find` is an integer such that 1 <= `find` <= `n`. `l` is the smallest index in `array` such that `array[l]` is greater than or equal to `find`, or `l` is `n` if `find` is greater than all elements in `array`. `r` is the largest index in `array` such that `array[r]` is less than `find`, or `r` is `-1` if `find` is less than or equal to all elements in `array`.
    if (l != array.index(find)) :
        print(1)
        #This is printed: 1
        return [str(l + 1), str(array.index(find) + 1)]
        #The program returns a list containing two strings: the first string is the smallest index `l` (plus 1) in `array` where `array[l]` is greater than or equal to `find`, and the second string is the index of `find` in `array` (plus 1).
    else :
        print(0)
        #This is printed: 0
    #State: `n` is equal to the length of the `array`, `array` is a list of integers representing a permutation of size `n` where 1 <= `n` <= 2 * 10^5, and all elements in `array` are distinct integers from 1 to `n`. `find` is an integer such that 1 <= `find` <= `n`. `l` is the smallest index in `array` such that `array[l]` is greater than or equal to `find`, or `l` is `n` if `find` is greater than all elements in `array`. `r` is the largest index in `array` such that `array[r]` is less than `find`, or `r` is `-1` if `find` is less than or equal to all elements in `array`. Additionally, `l` is equal to the index of `find` in `array`.
#Overall this is what the function does:The function `func_1` accepts a list `array` of distinct integers from 1 to n and an integer `find` within the same range. It returns a list of two strings: the first string is the smallest index (plus 1) where the element in `array` is greater than or equal to `find`, and the second string is the index (plus 1) of `find` in `array`. If `find` is not found in `array`, the function still returns the smallest index (plus 1) where the element in `array` is greater than or equal to `find`, and the index (plus 1) where `find` would be inserted to maintain the sorted order.


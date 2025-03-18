#State of the program right berfore the function call: array is a list of integers representing a permutation of length n (1 ≤ n ≤ 2·10^5) containing distinct integers from 1 to n, and find is an integer (1 ≤ find ≤ n) that needs to be found using a modified binary search algorithm. The function will be called multiple times with different test cases, and the sum of the values of n for all test cases does not exceed 2·10^5.
def func_1(array, find):
    n = len(array)
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        
        if array[mid] >= find:
            r = mid - 1
        else:
            l = mid + 1
        
    #State: `l` is the smallest index such that `array[l]` is greater than or equal to `find`, or `l` is `n` if `find` is greater than all elements in `array`. `r` is `l - 1`.
    if (l != array.index(find)) :
        print(1)
        #This is printed: 1
        return [str(l + 1), str(array.index(find) + 1)]
        #The program returns a list containing the string representation of `l + 1` and the string representation of the index of `find` in `array` plus 1.
    else :
        print(0)
        #This is printed: 0
    #State: `l` is the smallest index such that `array[l]` is greater than or equal to `find`, or `l` is `n` if `find` is greater than all elements in `array`. `r` is `l - 1`. `l` is equal to `array.index(find)` if `find` is in `array`.
#Overall this is what the function does:The function accepts a list of integers `array` representing a permutation of distinct integers from 1 to n, and an integer `find` to locate within the array. It returns a list containing the string representation of `l + 1` (where `l` is the smallest index such that `array[l]` is greater than or equal to `find`, or `n` if `find` is greater than all elements in `array`) and the string representation of the index of `find` in `array` plus 1 if `find` is in `array`. If `find` is not at the position indicated by `l`, it prints 1; otherwise, it prints 0.


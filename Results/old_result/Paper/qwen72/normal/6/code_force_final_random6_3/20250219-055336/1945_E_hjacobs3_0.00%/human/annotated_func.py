#State of the program right berfore the function call: array is a list of integers representing a permutation of size n (1 <= n <= 2 * 10^5), and find is an integer such that 1 <= find <= n.
def func_1(array, find):
    n = len(array)
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        
        if array[mid] >= find:
            r = mid - 1
        else:
            l = mid + 1
        
    #State: `array` is a list of integers representing a permutation of size `n`, `find` is an integer such that 1 <= `find` <= `n`, `n` is the length of `array`, `l` is the smallest index such that `array[l]` >= `find`, and `r` is `l` - 1.
    if (l != array.index(find)) :
        print(1)
        #This is printed: 1
        return [str(l + 1), str(array.index(find) + 1)]
        #The program returns a list containing two strings: the first string is the value of `l + 1` converted to a string, and the second string is the index of `find` in `array` plus 1, also converted to a string.
    else :
        print(0)
        #This is printed: 0
    #State: *`array` is a list of integers representing a permutation of size `n`, `find` is an integer such that 1 <= `find` <= `n`, `n` is the length of `array`, `l` is the smallest index such that `array[l]` >= `find`, and `r` is `l` - 1. Additionally, `l` is equal to the index of `find` in `array`.
#Overall this is what the function does:The function `func_1` accepts a list `array` of integers representing a permutation of size `n` and an integer `find` within the range 1 to `n`. It performs a binary search to find the smallest index `l` such that `array[l]` is greater than or equal to `find`. If `l` is not equal to the index of `find` in `array`, it prints `1` and returns a list containing two strings: the first string is the value of `l + 1` converted to a string, and the second string is the index of `find` in `array` plus 1, also converted to a string. If `l` is equal to the index of `find` in `array`, it prints `0` and does not return anything.


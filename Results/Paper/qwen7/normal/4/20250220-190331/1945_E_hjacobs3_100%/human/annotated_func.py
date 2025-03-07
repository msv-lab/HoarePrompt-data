#State of the program right berfore the function call: array is a list of integers representing a permutation of size n, and find is an integer such that 1 <= find <= n.
def func_1(array, find):
    n = len(array)
    l, r = 0, n
    while r - l > 1:
        mid = (l + r) // 2
        
        if array[mid] <= find:
            l = mid
        else:
            r = mid
        
    #State: Output State: The array is a list of integers representing a permutation of size n, `l` and `r` are such that `r - l` is no longer greater than 1, and `mid` is the last calculated midpoint value during the loop's execution. The loop has terminated because `r - l` is no longer greater than 1, meaning `l` and `r` are adjacent indices in the array.
    #
    #In simpler terms, after all iterations of the loop, `l` and `r` will point to two consecutive elements in the array, and `mid` will be the midpoint between `l` and `r` from the last iteration of the loop. The loop has effectively narrowed down the search range to a single element or a pair of elements, but since the exact position of `find` relative to the array elements is not specified, we can only conclude that `l` and `r` are adjacent.
    if (l != array.index(find)) :
        print(1)
        #This is printed: 1
        return [str(l + 1), str(array.index(find) + 1)]
        #The program returns a list containing two strings: the first string is the index of `l` incremented by 1, and the second string is the index of `find` in the array incremented by 1.
    else :
        print(0)
        #This is printed: 0
    #State: The array is a list of integers representing a permutation of size n, `l` and `r` are such that `r - l` is no longer greater than 1, and `mid` is the last calculated midpoint value during the loop's execution. `l` and `r` point to two consecutive elements in the array, and `l` is equal to `array.index(find)`.
#Overall this is what the function does:The function accepts a list of integers `array` representing a permutation of size `n` and an integer `find` such that 1 ≤ `find` ≤ `n`. It performs a binary search to find the index of `find` in `array`. If `find` is not found, it prints "1" and returns a list containing the index of `l` incremented by 1 and the index of `find` in `array` incremented by 1. If `find` is found, it prints "0" and returns the same list as above.


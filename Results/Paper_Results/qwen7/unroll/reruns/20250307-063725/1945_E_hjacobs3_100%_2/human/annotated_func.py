#State of the program right berfore the function call: array is a list of integers representing a permutation of length n, and find is an integer such that 1 <= find <= n.
def func_1(array, find):
    n = len(array)
    l, r = 0, n
    while r - l > 1:
        mid = (l + r) // 2
        
        if array[mid] <= find:
            l = mid
        else:
            r = mid
        
    #State: Output State: `l` is the index such that for all `i < l`, `array[i] > find`, and for all `i > l`, `array[i] >= find`. `r` is `l + 1`.
    #
    #Explanation: The loop is performing a binary search on the list `array` to find the position where the value `find` would fit in the sorted order of the list. After the loop finishes, `l` will point to the first index where `array[l]` is no longer less than or equal to `find`, and `r` will be `l + 1`. This means that all elements before `l` are less than or equal to `find`, and all elements from `l` onwards are greater than or equal to `find`.
    if (l != array.index(find)) :
        print(1)
        #This is printed: 1
        return [str(l + 1), str(array.index(find) + 1)]
        #The program returns a list containing two strings: "l + 1" and "array.index(find) + 1"
    else :
        print(0)
        #This is printed: 0
    #State: `l` is the index such that for all `i < l`, `array[i] > find`, and for all `i > l`, `array[i] >= find`. `r` is `l + 1`, and `l` equals `array.index(find)`
#Overall this is what the function does:The function accepts a list of integers `array` representing a permutation of length `n` and an integer `find` such that `1 <= find <= n`. It performs a binary search to find the position where `find` would fit in the sorted order of `array`. If `find` is not already in `array`, it returns a list containing the indices `l + 1` and `array.index(find) + 1`. If `find` is already in `array`, it returns a list containing the same indices but prints `0`.


#State of the program right berfore the function call: array is a list of integers representing a permutation of size n, and find is an integer such that 1 <= find <= n.
def func_1(array, find):
    n = len(array)
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        
        if array[mid] >= find:
            r = mid - 1
        else:
            l = mid + 1
        
    #State: The variable `l` will be equal to `r` + 1, and `r` will be the index of the last element in the list `array` that is less than `find`, or 0 if no such element exists.
    if (l != array.index(find)) :
        print(1)
        #This is printed: 1
        return [str(l + 1), str(array.index(find) + 1)]
        #The program returns a list containing two strings: "l + 1" and "array.index(find) + 1"
    else :
        print(0)
        #This is printed: 0
    #State: The variable `l` will be equal to `r` + 1, and `r` will be the index of the last element in the list `array` that is less than `find`, or 0 if no such element exists. Additionally, `l` is equal to `array.index(find)`.
#Overall this is what the function does:The function accepts a list of integers `array` representing a permutation of size `n` and an integer `find` such that `1 <= find <= n`. It performs a binary search to find the position where `find` would fit in the sorted version of `array`. If `find` is present in `array`, it returns a list containing the positions of `l + 1` and `array.index(find) + 1`. If `find` is not present, it returns a list containing the positions of `l + 1` and the position just before where `find` would be inserted. The function prints `1` if `find` is present and `0` if it is not.


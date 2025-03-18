#State of the program right berfore the function call: array is a list of integers representing a permutation of size n (1 ≤ n ≤ 2·10^5), and find is an integer (1 ≤ find ≤ n) that needs to be found in the permutation.
def func_1(array, find):
    n = len(array)
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        
        if array[mid] >= find:
            r = mid - 1
        else:
            l = mid + 1
        
    #State: `l` is the index of the first element in `array` that is greater than or equal to `find`, and `r` is the index of the last element in `array` that is less than `find`. If `find` is greater than all elements in `array`, `l` will be `n` and `r` will be `n - 1`. If `find` is less than or equal to all elements in `array`, `l` will be `0` and `r` will be `-1`.
    if (l != array.index(find)) :
        print(1)
        #This is printed: 1
        return [str(l + 1), str(array.index(find) + 1)]
        #The program returns a list containing two string values: the first is the string representation of `l + 1`, where `l` is the index of the first element in `array` that is greater than or equal to `find`, and the second is the string representation of the index of `find` in `array` plus 1.
    else :
        print(0)
        #This is printed: 0
    #State: `l` is the index of the first element in `array` that is greater than or equal to `find`, and `r` is the index of the last element in `array` that is less than `find`. If `find` is greater than all elements in `array`, `l` will be `n` and `r` will be `n - 1`. If `find` is less than or equal to all elements in `array`, `l` will be `0` and `r` will be `-1`. Additionally, `l` is equal to the index of `find` in `array`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `array` and an integer `find`. It performs a binary search to find the position of `find` in the sorted permutation `array`. The function returns a list of two strings: the first string is the 1-based index of the first element in `array` that is greater than or equal to `find`, and the second string is the 1-based index of `find` in `array` if it exists. If `find` is not found at the position `l`, the function prints `1` and returns the list as described. If `find` is found at the position `l`, the function prints `0` and does not return anything.


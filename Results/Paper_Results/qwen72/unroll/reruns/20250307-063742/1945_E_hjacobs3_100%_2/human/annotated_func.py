#State of the program right berfore the function call: array is a list of integers representing a permutation of size n (1 ≤ n ≤ 2·10^5), and find is an integer such that 1 ≤ find ≤ n.
def func_1(array, find):
    n = len(array)
    l, r = 0, n
    while r - l > 1:
        mid = (l + r) // 2
        
        if array[mid] <= find:
            l = mid
        else:
            r = mid
        
    #State: `l` is the largest index such that `array[l]` is less than or equal to `find`, and `r` is the smallest index such that `array[r]` is greater than `find`.
    if (l != array.index(find)) :
        print(1)
        #This is printed: 1
        return [str(l + 1), str(array.index(find) + 1)]
        #The program returns a list containing two string values: the first value is the string representation of `l + 1`, where `l` is the largest index such that `array[l]` is less than or equal to `find`; the second value is the string representation of the index of `find` in the array plus 1.
    else :
        print(0)
        #This is printed: 0
    #State: *`l` is the largest index such that `array[l]` is less than or equal to `find`, and `r` is the smallest index such that `array[r]` is greater than `find`. Additionally, `l` is equal to the index of `find` in `array`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `array` and an integer `find`. It returns a list of two strings: the first string is the 1-based index of the largest element in `array` that is less than or equal to `find`, and the second string is the 1-based index of `find` in `array` if `find` exists in `array`. If `l` (the largest index such that `array[l]` is less than or equal to `find`) is not equal to the index of `find` in `array`, it prints `1` and returns the list. If `l` is equal to the index of `find` in `array`, it prints `0` and does not return anything.


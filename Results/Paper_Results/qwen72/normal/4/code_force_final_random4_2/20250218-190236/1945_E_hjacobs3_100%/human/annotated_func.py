#State of the program right berfore the function call: array is a permutation of integers from 1 to n, and find is an integer such that 1 <= find <= n.
def func_1(array, find):
    n = len(array)
    l, r = 0, n
    while r - l > 1:
        mid = (l + r) // 2
        
        if array[mid] <= find:
            l = mid
        else:
            r = mid
        
    #State: `array` is a permutation of integers from 1 to n, `find` is an integer such that 1 <= find <= n, `n` is the length of `array`, `l` and `r` are such that `r - l` is at most 1, and `array[l]` is the largest element in `array` that is less than or equal to `find`, or `l` is 0 and `r` is 1 if `find` is less than `array[0]`.
    if (l != array.index(find)) :
        print(1)
        #This is printed: 1
        return [str(l + 1), str(array.index(find) + 1)]
        #The program returns a list containing two string values: the first value is the string representation of `l + 1`, where `l` is the index of the largest element in `array` that is less than or equal to `find`, or 0 if `find` is less than `array[0]`. The second value is the string representation of the index of `find` in `array` plus 1.
    else :
        print(0)
        #This is printed: 0
    #State: `array` is a permutation of integers from 1 to n, `find` is an integer such that 1 <= find <= n, `n` is the length of `array`, `l` and `r` are such that `r - l` is at most 1, and `array[l]` is the largest element in `array` that is less than or equal to `find`, or `l` is 0 and `r` is 1 if `find` is less than `array[0]`. Additionally, `l` is equal to the index of `find` in `array`.
#Overall this is what the function does:The function `func_1` accepts an array (a permutation of integers from 1 to n) and an integer `find` (1 <= find <= n). It returns a list of two string values: the first value is the string representation of the index (plus 1) of the largest element in the array that is less than or equal to `find`, or "1" if `find` is less than the first element of the array. The second value is the string representation of the index of `find` in the array plus 1. If the index `l` is not equal to the index of `find` in the array, the function prints "1"; otherwise, it prints "0".


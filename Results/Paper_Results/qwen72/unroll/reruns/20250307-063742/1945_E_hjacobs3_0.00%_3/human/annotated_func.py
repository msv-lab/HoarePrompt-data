#State of the program right berfore the function call: array is a permutation of size n (1 ≤ n ≤ 2·10^5) consisting of distinct integers from 1 to n, and find is an integer (1 ≤ find ≤ n) that needs to be found in the permutation.
def func_1(array, find):
    n = len(array)
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        
        if array[mid] >= find:
            r = mid - 1
        else:
            l = mid + 1
        
    #State: `l` is the index of the first element in `array` that is greater than or equal to `find`, and `r` is `l` - 1.
    if (l != array.index(find)) :
        print(1)
        #This is printed: 1
        return [str(l + 1), str(array.index(find) + 1)]
        #The program returns a list containing two strings: the first string is the value of `l + 1` converted to a string, and the second string is the value of the index of `find` in `array` plus 1, also converted to a string.
    else :
        print(0)
        #This is printed: 0
    #State: *`l` is the index of the first element in `array` that is greater than or equal to `find`, and `r` is `l` - 1. `l` is equal to the index of `find` in `array`.
#Overall this is what the function does:The function `func_1` accepts an array (a permutation of size n consisting of distinct integers from 1 to n) and an integer `find` (1 ≤ find ≤ n). It returns a list containing two strings: the first string is the value of `l + 1` (where `l` is the index of the first element in `array` that is greater than or equal to `find`), and the second string is the value of the index of `find` in `array` plus 1, both converted to strings. If `l` is not equal to the index of `find` in `array`, it prints `1`; otherwise, it prints `0`.


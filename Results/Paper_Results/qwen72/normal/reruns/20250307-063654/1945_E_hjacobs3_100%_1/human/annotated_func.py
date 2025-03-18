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
        
    #State: `array` is a list of integers representing a permutation of size `n`, `find` is an integer such that 1 ≤ `find` ≤ `n`, `n` is the length of `array`, and `n` must be greater than 1. After the loop finishes, `l` is the largest index such that `array[l]` ≤ `find`, and `r` is the smallest index such that `array[r]` > `find`.
    if (l != array.index(find)) :
        print(1)
        #This is printed: 1
        return [str(l + 1), str(array.index(find) + 1)]
        #The program returns a list containing two strings: the first string is the value of `l + 1` converted to a string, where `l` is the largest index such that `array[l]` ≤ `find`; the second string is the value of `array.index(find) + 1` converted to a string, which is the index of `find` in `array` plus 1.
    else :
        print(0)
        #This is printed: 0
    #State: `array` is a list of integers representing a permutation of size `n`, `find` is an integer such that 1 ≤ `find` ≤ `n`, `n` is the length of `array`, and `n` must be greater than 1. After the loop finishes, `l` is the largest index such that `array[l]` ≤ `find`, and `r` is the smallest index such that `array[r]` > `find`. Additionally, `l` is equal to the index of `find` in `array`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `array` and an integer `find`. It returns a list of two strings if `l` (the largest index such that `array[l]` ≤ `find`) is not equal to the index of `find` in `array`. The first string is the 1-based index of the largest element in `array` that is less than or equal to `find`, and the second string is the 1-based index of `find` in `array`. If `l` is equal to the index of `find` in `array`, the function prints `0` and returns `None`. The function does not modify the input `array`.


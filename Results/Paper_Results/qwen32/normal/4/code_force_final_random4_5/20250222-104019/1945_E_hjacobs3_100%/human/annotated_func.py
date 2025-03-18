#State of the program right berfore the function call: array is a list of integers representing a permutation of length n (1 ≤ n ≤ 2⋅10^5) containing distinct integers from 1 to n, and find is an integer (1 ≤ find ≤ n) that needs to be found in the permutation.
def func_1(array, find):
    n = len(array)
    l, r = 0, n
    while r - l > 1:
        mid = (l + r) // 2
        
        if array[mid] <= find:
            l = mid
        else:
            r = mid
        
    #State: `l` is the largest index such that `array[l] <= find`, and `r` is the smallest index such that `array[r] > find` (or `n` if no such element exists).
    if (l != array.index(find)) :
        print(1)
        #This is printed: 1
        return [str(l + 1), str(array.index(find) + 1)]
        #The program returns a list containing two strings. The first string is the value of `l + 1`, and the second string is the value of the index of `find` in the array plus one.
    else :
        print(0)
        #This is printed: 0
    #State: `l` is the largest index such that `array[l] <= find`, and `r` is the smallest index such that `array[r] > find` (or `n` if no such element exists). Additionally, `l` is equal to the index of `find` in the array.
#Overall this is what the function does:The function takes a list `array` representing a permutation of integers from 1 to n and an integer `find`. It returns a list containing two strings: the first string is the largest index `l + 1` such that the element at index `l` is less than or equal to `find`, and the second string is the index of `find` in the array plus one. If `l` is not equal to the index of `find`, it prints 1; otherwise, it prints 0.


#State of the program right berfore the function call: array is a list of integers representing a permutation of length n (1 ≤ n ≤ 2⋅10^5), and find is an integer (1 ≤ find ≤ n) that needs to be found in the permutation. The sum of the values of n for all test cases does not exceed 2⋅10^5.
def func_1(array, find):
    n = len(array)
    l, r = 0, n
    while r - l > 1:
        mid = (l + r) // 2
        
        if array[mid] <= find:
            l = mid
        else:
            r = mid
        
    #State: `array` is a list of integers representing a permutation of length `n`; `find` is an integer (1 ≤ find ≤ n); `l` is the index of the largest element in `array` that is less than or equal to `find`; `r` is `l + 1`.
    if (l != array.index(find)) :
        print(1)
        #This is printed: 1
        return [str(l + 1), str(array.index(find) + 1)]
        #The program returns a list containing two strings: the first string is the index (1-based) of the largest element in `array` that is less than or equal to `find`, and the second string is the index (1-based) of `find` in `array`.
    else :
        print(0)
        #This is printed: 0
    #State: `array` is a list of integers representing a permutation of length `n`; `find` is an integer (1 ≤ find ≤ n); `l` is the index of the largest element in `array` that is less than or equal to `find`; `r` is `l + 1`; `l` is equal to the index of the element `find` in `array`
#Overall this is what the function does:The function takes a list of integers representing a permutation and an integer to find within that permutation. It returns a list containing two strings: the first string is the 1-based index of the largest element in the list that is less than or equal to the integer to find, and the second string is the 1-based index of the integer to find in the list. If the largest element less than or equal to the integer to find is the same as the integer to find itself, it prints 0; otherwise, it prints 1.


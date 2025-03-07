#State of the program right berfore the function call: array is a permutation of integers from 1 to n, where n is the length of the array, and find is an integer such that 1 <= find <= n.
def func_1(array, find):
    n = len(array)
    l, r = 0, n
    while r - l > 1:
        mid = (l + r) // 2
        
        if array[mid] <= find:
            l = mid
        else:
            r = mid
        
    #State: `array` is a permutation of integers from 1 to `n`, `find` is an integer such that 1 <= `find` <= `n`, `n` is the length of the array, `l` is the largest index such that `array[l] <= find`, and `r` is `l + 1`.
    if (l != array.index(find)) :
        print(1)
        #This is printed: 1
        return [str(l + 1), str(array.index(find) + 1)]
        #The program returns a list containing two strings: the first string is the value of `l + 1`, and the second string is the value of the index of `find` in `array` plus 1.
    else :
        print(0)
        #This is printed: 0
    #State: `array` is a permutation of integers from 1 to `n`, `find` is an integer such that 1 <= `find` <= `n`, `n` is the length of the array, `l` is the largest index such that `array[l] <= find`, `r` is `l + 1`, and `l` is equal to the index of `find` in `array`
#Overall this is what the function does:The function takes an array, which is a permutation of integers from 1 to n, and an integer `find` such that 1 <= `find` <= n. It returns a list containing two strings: the first string is the value of `l + 1`, where `l` is the largest index such that `array[l] <= find`, and the second string is the value of the index of `find` in `array` plus 1. If `l` is not equal to the index of `find` in `array`, it prints 1; otherwise, it prints 0.


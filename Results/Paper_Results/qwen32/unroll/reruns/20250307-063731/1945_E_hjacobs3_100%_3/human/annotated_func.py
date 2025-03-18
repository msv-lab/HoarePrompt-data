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
        
    #State: l is the largest index such that array[l] <= find, and r is l + 1.
    if (l != array.index(find)) :
        print(1)
        #This is printed: 1
        return [str(l + 1), str(array.index(find) + 1)]
        #The program returns [str(l + 1), str(array.index(find) + 1)], where l is the largest index such that array[l] <= find, and array.index(find) is the index of the first occurrence of find in the array.
    else :
        print(0)
        #This is printed: 0
    #State: `l` is the largest index such that `array[l] <= find`, and `r` is `l + 1`. `l` is equal to `array.index(find)`
#Overall this is what the function does:The function accepts a list of integers `array` representing a permutation and an integer `find`. It returns a list of two strings: the first string is the 1-based index of the largest position in `array` where the value is less than or equal to `find`, and the second string is the 1-based index of the first occurrence of `find` in `array`. If the largest index `l` such that `array[l] <= find` is not the same as the index of the first occurrence of `find`, it prints `1`; otherwise, it prints `0`.


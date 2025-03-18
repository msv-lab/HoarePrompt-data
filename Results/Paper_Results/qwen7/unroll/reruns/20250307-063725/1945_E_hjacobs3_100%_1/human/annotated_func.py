#State of the program right berfore the function call: array is a list of integers representing a permutation of size n, and find is an integer such that 1 <= find <= n.
def func_1(array, find):
    n = len(array)
    l, r = 0, n
    while r - l > 1:
        mid = (l + r) // 2
        
        if array[mid] <= find:
            l = mid
        else:
            r = mid
        
    #State: l and r are such that l == r - 1 and array[l] either equals or is greater than 'find', while array[r] is either less than 'find' or does not exist.
    if (l != array.index(find)) :
        print(1)
        #This is printed: 1
        return [str(l + 1), str(array.index(find) + 1)]
        #The program returns ['l + 1', 'find' index in array + 1]
    else :
        print(0)
        #This is printed: 0
    #State: `l` and `r` are such that `l == r - 1`, and `array[l]` either equals or is greater than `'find'`, while `array[r]` is either less than `'find'` or does not exist. The index of `'find'` in `array` is equal to `l`.
#Overall this is what the function does:The function accepts a list `array` of integers representing a permutation of size `n` and an integer `find` such that `1 <= find <= n`. It performs a binary search to find the position of `find` in `array`. If `find` is not in `array`, it prints `1` and returns the indices `['l + 1', 'find' index in array + 1]`. If `find` is found in `array`, it prints `0` and returns the same indices.


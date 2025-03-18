#State of the program right berfore the function call: array is a list of integers representing a permutation of size n, and find is an integer such that 1 ≤ find ≤ n.
def func_1(array, find):
    n = len(array)
    l, r = 0, n
    while r - l > 1:
        mid = (l + r) // 2
        
        if array[mid] <= find:
            l = mid
        else:
            r = mid
        
    #State: The variables `l` and `r` will define a range such that `array[l]` is the largest value less than or equal to `find`, or `l` will be equal to `n` if no such element exists.
    if (l != array.index(find)) :
        print(1)
        #This is printed: 1
        return [str(l + 1), str(array.index(find) + 1)]
        #The program returns a list containing two strings: the first string is 'l + 1', and the second string is the index of 'find' in 'array' incremented by 1.
    else :
        print(0)
        #This is printed: 0
    #State: The variables `l` and `r` define a range such that `array[l]` is the largest value less than or equal to `find`, or `l` will be equal to `n` if no such element exists. Additionally, `l` is equal to `array.index(find)`.
#Overall this is what the function does:The function accepts a list of integers (`array`) representing a permutation of size `n` and an integer (`find`) such that `1 ≤ find ≤ n`. It searches for the largest element in `array` that is less than or equal to `find`. If such an element exists and its index is different from the index of `find`, it returns a list containing two strings: the first string is the index of the found element incremented by 1, and the second string is the index of `find` incremented by 1. If no such element exists or if the largest element is `find` itself, it returns a list containing two zeros.


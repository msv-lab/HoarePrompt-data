#State of the program right berfore the function call: array is a list of integers representing a permutation of size n, and find is an integer such that 1 <= find <= n.
def func_1(array, find):
    n = len(array)
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        
        if array[mid] >= find:
            r = mid - 1
        else:
            l = mid + 1
        
    #State: The variable `l` will be equal to `r` + 1, and `r` will be the index of the last element in the array that is less than `find`, or `r` will be -1 if no such element exists.
    if (l != array.index(find)) :
        print(1)
        #This is printed: 1
        return [str(l + 1), str(array.index(find) + 1)]
        #The program returns a list containing two strings: the first string is the value of `l + 1` converted to a string, and the second string is the index of `find` in the array converted to a string and incremented by 1.
    else :
        print(0)
        #This is printed: 0
    #State: The variable `l` will be equal to `r` + 1, and `r` will be the index of the last element in the array that is less than `find`, or `r` will be -1 if no such element exists. Additionally, `l` is equal to `array.index(find)`
#Overall this is what the function does:The function accepts a list of integers (`array`) representing a permutation of size `n` and an integer (`find`) such that `1 <= find <= n`. It performs a binary search to find the position of `find` in the array. If `find` is found, it returns a list containing two strings: the first string is the index of `find` incremented by 1, and the second string is the index of `find` itself incremented by 1. If `find` is not found, it prints `1` and returns a list containing two strings: the first string is the index where `find` should be inserted to maintain the order, and the second string is `-1`.


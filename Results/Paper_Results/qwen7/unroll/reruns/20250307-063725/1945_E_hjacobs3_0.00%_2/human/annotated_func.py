#State of the program right berfore the function call: array is a list of integers representing a permutation of length n, and find is an integer such that 1 <= find <= n.
def func_1(array, find):
    n = len(array)
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        
        if array[mid] >= find:
            r = mid - 1
        else:
            l = mid + 1
        
    #State: Output State: `l` is greater than `r`.
    #
    #Explanation: The loop continues as long as `l` is less than or equal to `r`. Inside the loop, we calculate `mid` as the integer division of the sum of `l` and `r` by 2. Depending on whether `array[mid]` is greater than or equal to `find`, we adjust either `l` to `mid + 1` or `r` to `mid - 1`. This process narrows down the search range until `l` becomes greater than `r`, at which point the loop terminates. At this point, `l` will be the smallest index such that `array[l]` is greater than `find`, or `n` if no such element exists.
    if (l != array.index(find)) :
        print(1)
        #This is printed: 1
        return [str(l + 1), str(array.index(find) + 1)]
        #The program returns a list containing two strings: the first string is the value of `l + 1` converted to a string, and the second string is the index of `find` in `array` converted to a string and incremented by 1.
    else :
        print(0)
        #This is printed: 0
    #State: `l` is greater than `r`, and `l` is equal to the index of `find` in the array
#Overall this is what the function does:The function accepts a list of integers (`array`) representing a permutation of length `n` and an integer (`find`) such that `1 <= find <= n`. It performs a binary search to find the position of `find` in `array`. If `find` is present in `array`, it returns a list containing two strings: the first string is the index of `find` in `array` incremented by 1, and the second string is the same index incremented by 1. If `find` is not present, it returns a list containing two strings: "1" and the index where `find` would be inserted to maintain the order, both incremented by 1.


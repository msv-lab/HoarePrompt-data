#State of the program right berfore the function call: array is a list of integers representing a permutation of size n (1 ≤ n ≤ 2·10^5), and find is an integer such that 1 ≤ find ≤ n.
def func_1(array, find):
    n = len(array)
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        
        if array[mid] >= find:
            r = mid - 1
        else:
            l = mid + 1
        
    #State: The loop will terminate with `l` being the index of the first element in `array` that is greater than or equal to `find`, and `r` being the index of the last element in `array` that is less than `find`. If `find` is greater than all elements in `array`, `l` will be `n` and `r` will be `n - 1`. If `find` is less than or equal to the first element in `array`, `l` will be `0` and `r` will be `-1`.
    if (l != array.index(find)) :
        print(1)
        #This is printed: 1
        return [str(l + 1), str(array.index(find) + 1)]
        #The program returns a list containing two strings: the first string is the value of `l + 1` converted to a string, and the second string is the value of the index of the first occurrence of `find` in `array` plus 1, also converted to a string. Note that `l` is the index of the first element in `array` that is greater than or equal to `find`, and `array.index(find)` is the index of the first occurrence of `find` in `array`.
    else :
        print(0)
        #This is printed: 0
    #State: The loop will terminate with `l` being the index of the first element in `array` that is greater than or equal to `find`, and `r` being the index of the last element in `array` that is less than `find`. If `find` is greater than all elements in `array`, `l` will be `n` and `r` will be `n - 1`. If `find` is less than or equal to the first element in `array`, `l` will be `0` and `r` will be `-1`. Additionally, `l` is equal to the index of `find` in `array`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `array` and an integer `find`. It returns a list of two strings. The first string represents the 1-based index of the first element in `array` that is greater than or equal to `find`. The second string represents the 1-based index of the first occurrence of `find` in `array`. If `find` is not present in `array`, the function still returns the 1-based index of the first element that is greater than or equal to `find`, and the second string will be the 1-based index of the element immediately before `find` would be inserted to maintain the sorted order. The function prints `1` if the index of the first element greater than or equal to `find` is different from the index of `find` in `array`, and `0` otherwise.


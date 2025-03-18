#State of the program right berfore the function call: arr is a list of elements that can be compared to each other.
def func_1(arr):
    n = len(arr)
    for size in range(n, 0, -1):
        max_index = arr.index(max(arr[:size]))
        
        if max_index != size - 1:
            if max_index != 0:
                arr[:max_index + 1] = arr[:max_index + 1][::-1]
            arr[:size] = arr[:size][::-1]
        
    #State of the program after the  for loop has been executed: `arr` is a sorted list of elements in ascending order, `n` is the original length of `arr`.
    return arr
    #The program returns the sorted list 'arr' of elements in ascending order
#Overall this is what the function does:The function accepts a list `arr` of comparable elements and sorts it in ascending order using a selection sort-like algorithm that reverses segments of the list. It returns the sorted list `arr`.


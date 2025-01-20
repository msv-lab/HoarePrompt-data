#State of the program right berfore the function call: arr is a list of comparable elements.
def func_1(arr):
    n = len(arr)
    for size in range(n, 0, -1):
        max_index = arr.index(max(arr[:size]))
        
        if max_index != size - 1:
            if max_index != 0:
                arr[:max_index + 1] = arr[:max_index + 1][::-1]
            arr[:size] = arr[:size][::-1]
        
    #State of the program after the  for loop has been executed: `arr` is a list of comparable elements sorted in ascending order, `n` is the length of `arr`, `size` is 0. The loop ensures that after each iteration, the largest unsorted element is moved to its correct position at the end of the unsorted portion of the list. This process continues until the entire list is sorted. Variables `n` and `arr` remain constant throughout the loop, while `size` decreases from `n` to 1. The loop always executes `n` times, assuming `n > 0`.
    return arr
    #The program returns the list `arr` which is a list of comparable elements sorted in ascending order. The length of `arr` is `n`. After the loop, the list remains sorted in ascending order, and `size` has decreased from `n` to 1.
#Overall this is what the function does:The function `func_1` accepts a list `arr` of comparable elements and returns the list sorted in ascending order. The length of the returned list remains the same as the input list. The function uses a series of reversals to ensure that the largest unsorted element is moved to its correct position at the end of the unsorted portion of the list in each iteration. After the function concludes, the list `arr` is guaranteed to be sorted in ascending order, and the variable `size` will have decreased from the initial length of `arr` to 1. If the input list is empty or contains only one element, it is returned unchanged.


#State of the program right berfore the function call: arr is a list of elements that can be compared to each other.
def func_1(arr):
    n = len(arr)
    for size in range(n, 0, -1):
        max_index = arr.index(max(arr[:size]))
        
        if max_index != size - 1:
            if max_index != 0:
                arr[:max_index + 1] = arr[:max_index + 1][::-1]
            arr[:size] = arr[:size][::-1]
        
    #State of the program after the  for loop has been executed: `arr` is a sorted list in ascending order, `n` is the length of the original list (non-negative integer).
    return arr
    #The program returns the sorted list 'arr' in ascending order, where 'n' is the length of the original list (non-negative integer).
#Overall this is what the function does:The function `func_1` accepts a list of elements `arr` that can be compared to each other and sorts the list in ascending order using a series of reversals. After execution, the function returns the sorted list `arr`. It is important to note that if the input list is already sorted or contains identical elements, the function will still return the input list as it is, without modifying it. The function does not handle cases where the input is `None` or contains non-comparable types, which could lead to exceptions during execution. The length of the original list is preserved as part of the sorting process.


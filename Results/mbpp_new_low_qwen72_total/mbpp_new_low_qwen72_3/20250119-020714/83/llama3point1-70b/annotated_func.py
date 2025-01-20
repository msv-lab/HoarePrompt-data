#State of the program right berfore the function call: arr is a list of elements that can be compared with each other.
def func_1(arr):
    n = len(arr)
    for size in range(n, 0, -1):
        max_index = arr.index(max(arr[:size]))
        
        if max_index != size - 1:
            if max_index != 0:
                arr[:max_index + 1] = arr[:max_index + 1][::-1]
            arr[:size] = arr[:size][::-1]
        
    #State of the program after the  for loop has been executed: `arr` is a sorted list in ascending order, `n` is the number of elements in `arr`, `size` is 0, and `max_index` is undefined. The loop ensures that after each iteration, the largest element in the unsorted portion of the array is moved to its correct position in the sorted portion of the array. The loop iterates `n` times, once for each element in the array, and upon completion, `arr` is fully sorted in ascending order.
    return arr
    #The program returns the list `arr` which is fully sorted in ascending order, containing `n` elements.
#Overall this is what the function does:The function `func_1` accepts a parameter `arr`, which is a list of comparable elements. It sorts the list `arr` in ascending order using a variation of the selection sort algorithm. The function modifies the list in place and returns the sorted list. After the function concludes, `arr` is fully sorted in ascending order, and contains `n` elements, where `n` is the length of the original list. The function handles edge cases such as empty lists and lists with duplicate elements correctly. However, the function does not handle non-comparable elements (e.g., mixing integers and strings) and will raise a `TypeError` if the elements in `arr` cannot be compared.


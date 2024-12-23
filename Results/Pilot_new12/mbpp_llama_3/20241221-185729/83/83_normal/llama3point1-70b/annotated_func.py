#State of the program right berfore the function call: arr is a list of elements.
def func_1(arr):
    n = len(arr)
    for size in range(n, 0, -1):
        max_index = arr.index(max(arr[:size]))
        
        if max_index != size - 1:
            if max_index != 0:
                arr[:max_index + 1] = arr[:max_index + 1][::-1]
            arr[:size] = arr[:size][::-1]
        
    #State of the program after the  for loop has been executed: `arr` is a sorted list in ascending order, `n` is the number of elements in the original list `arr`. If the original list `arr` was empty (i.e., `n` was 0), then `arr` remains an empty list.
    return arr
    #The program returns a sorted list 'arr' in ascending order, which contains 'n' number of elements, if 'n' is 0 then 'arr' remains an empty list
#Overall this is what the function does:The function accepts a list of elements as input and returns the same list sorted in ascending order. It handles the edge case where the input list is empty, in which case it returns the empty list as is. The function modifies the original list in place through its sorting operations. It does not add or remove any elements from the list, thus preserving the original number of elements. If the input list contains duplicate elements, they will be ordered accordingly in the sorted output. The function does not validate the type of elements in the list, implying it relies on the elements being comparable for sorting purposes.


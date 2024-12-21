#State of the program right berfore the function call: arr is a list of elements.
def func_1(arr):
    n = len(arr)
    for size in range(n, 0, -1):
        max_index = arr.index(max(arr[:size]))
        
        if max_index != size - 1:
            if max_index != 0:
                arr[:max_index + 1] = arr[:max_index + 1][::-1]
            arr[:size] = arr[:size][::-1]
        
    #State of the program after the  for loop has been executed: `arr` is sorted in descending order if the original `n` is greater than 0, otherwise `arr` remains unchanged; `n` is the original number of elements in `arr`.
    return arr
    #The program returns array 'arr' which is either sorted in descending order if the original 'n' is greater than 0, otherwise 'arr' remains unchanged, and 'n' is the original number of elements in 'arr'
#Overall this is what the function does:The function accepts a list of elements `arr` and returns the array sorted in descending order if the original number of elements in `arr` is greater than 0. If the original number of elements in `arr` is 0, the function returns the original array, which remains unchanged. The function handles potential edge cases, such as an empty input list or a list with a single element, and returns the original list in these cases. Additionally, the function modifies the input list `arr` in-place, meaning that the original list is modified during the sorting process. The function does not handle cases where the input is not a list or where the list contains uncomparable elements. After the function concludes, the state of the program is that the input list `arr` has been modified to be sorted in descending order if it was not empty, and the original number of elements in `arr` is preserved.


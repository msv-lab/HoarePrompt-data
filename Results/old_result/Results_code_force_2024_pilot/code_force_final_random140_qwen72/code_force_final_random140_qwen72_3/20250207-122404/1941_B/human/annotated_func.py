#State of the program right berfore the function call: array is a list of integers, and index is an integer such that 2 <= index < len(array) - 1.
def func_1(array, index):
    array[index - 1] = array[index - 1] - 1
    array[index] = array[index] - 2
    array[index + 1] = array[index + 1] - 1
    return array
    #The program returns the list `array` where the element at position `index - 1` is decreased by 1, the element at position `index` is decreased by 2, and the element at position `index + 1` is decreased by 1.
#Overall this is what the function does:The function `func_1` accepts a list of integers `array` and an integer `index` (where 2 <= index < len(array) - 1). It modifies the list `array` by decreasing the element at position `index - 1` by 1, the element at position `index` by 2, and the element at position `index + 1` by 1. The function then returns the modified list `array`.

#State of the program right berfore the function call: arrayForSuccess is a list of integers.
def func_2(arrayForSuccess):
    for x in arrayForSuccess:
        if x != 0:
            return False
        
    #State: The loop has completed all iterations, and `arrayForSuccess` is a list of integers where every integer is 0. The function does not return `False` during any iteration, indicating that no non-zero integers were encountered in the list.
    return True
    #The program returns True, indicating that the list `arrayForSuccess` did not contain any non-zero integers throughout all iterations.
#Overall this is what the function does:The function `func_2` accepts a list of integers `arrayForSuccess` and checks if all elements in the list are zero. If any element is non-zero, the function immediately returns `False`. If all elements are zero, the function returns `True`. After the function concludes, the list `arrayForSuccess` remains unchanged, and the function returns either `True` or `False` based on the presence of non-zero integers in the list.


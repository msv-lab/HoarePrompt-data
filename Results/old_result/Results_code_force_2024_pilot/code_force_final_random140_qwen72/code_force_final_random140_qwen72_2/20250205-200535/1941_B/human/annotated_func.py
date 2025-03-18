#State of the program right berfore the function call: array is a list of integers, and index is an integer such that 2 <= index < len(array) - 1.
def func_1(array, index):
    array[index - 1] = array[index - 1] - 1
    array[index] = array[index] - 2
    array[index + 1] = array[index + 1] - 1
    return array
    #The program returns the list `array` where the value at `array[index - 1]` is decreased by 1, the value at `array[index]` is decreased by 2, and the value at `array[index + 1]` is decreased by 1.
#Overall this is what the function does:The function `func_1` accepts a list of integers `array` and an integer `index` (where 2 <= index < len(array) - 1). It modifies the list by decreasing the value at `array[index - 1]` by 1, the value at `array[index]` by 2, and the value at `array[index + 1]` by 1. The function then returns the modified list `array`.

#State of the program right berfore the function call: arrayForSuccess is a list of integers.
def func_2(arrayForSuccess):
    for x in arrayForSuccess:
        if x != 0:
            return False
        
    #State: The loop will continue to iterate over all elements in `arrayForSuccess`. If any element `x` in the list is not equal to 0, the function will return `False` immediately. If all elements in the list are equal to 0, the loop will complete without returning `False`, and the function will implicitly return `None` (or the function will reach its end without returning a value).
    return True
    #The program returns `True`.
#Overall this is what the function does:The function `func_2` takes a list of integers `arrayForSuccess` as a parameter. It checks if all elements in the list are equal to 0. If any element is not 0, the function immediately returns `False`. If all elements are 0, the function returns `True`. In all other cases where the list contains at least one non-zero element, the function returns `False`.

#State of the program right berfore the function call: inputarray is a list of non-negative integers, and its length is at least 3.
def func_3(inputarray):
    if func_2(inputarray) :
        answers.append('YES')
        return
        #The program returns nothing. However, it's known that `inputarray` is a list of non-negative integers with a length of at least 3, `func_2` applied to `inputarray` returns `True`, and `answers` contains the string 'YES'.
    #State: inputarray is a list of non-negative integers, and its length is at least 3, and `func_2(inputarray)` returns `False`.
    loop_counter = 1
    while loop_counter != 100:
        length = len(inputarray)
        
        highestNumber = -1
        
        highestIndex = -1
        
        for elementIndex in range(1, length - 1):
            if inputarray[elementIndex] >= highestNumber:
                highestIndex = elementIndex
                highestNumber = inputarray[elementIndex]
        
        if highestNumber < 0:
            answers.append('NO')
            return
        
        newArray = func_1(inputarray, highestIndex)
        
        if func_2(newArray):
            answers.append('YES')
            return
        
        loop_counter += 1
        
    #State: After all iterations of the loop, `inputarray` remains a list of non-negative integers with a length of at least 3, `func_2(inputarray)` returns `False`, `loop_counter` is 100, `length` is the length of `inputarray`, `elementIndex` is `length - 1`, `highestNumber` is the highest value in `inputarray` from index 1 to `length - 2`, `highestIndex` is the index of the highest value in `inputarray` from index 1 to `length - 2`, `newArray` is the result of `func_1(inputarray, highestIndex)`, and `func_2(newArray)` returns `False`.
    answers.append('NO')
#Overall this is what the function does:The function `func_3` takes a list of non-negative integers `inputarray` with a minimum length of 3. It checks if a condition defined by `func_2` is met for `inputarray`. If `func_2(inputarray)` returns `True`, the function appends 'YES' to the global list `answers` and returns. If `func_2(inputarray)` returns `False`, the function enters a loop that iterates up to 100 times. In each iteration, it finds the highest number in `inputarray` (excluding the first and last elements) and applies `func_1` to `inputarray` using the index of the highest number. If `func_2` returns `True` for the new array, 'YES' is appended to `answers` and the function returns. If the loop completes without finding a suitable condition, 'NO' is appended to `answers`. The function does not return any value explicitly but modifies the global list `answers` to contain either 'YES' or 'NO'.


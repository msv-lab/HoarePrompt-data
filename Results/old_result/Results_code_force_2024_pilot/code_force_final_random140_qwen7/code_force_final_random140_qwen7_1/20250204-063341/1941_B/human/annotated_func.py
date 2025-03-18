#State of the program right berfore the function call: array is a list of integers, index is an integer such that 2 <= index <= len(array) - 1.
def func_1(array, index):
    array[index - 1] = array[index - 1] - 1
    array[index] = array[index] - 2
    array[index + 1] = array[index + 1] - 1
    return array
    #The program returns a list of integers where the element at index-1 is decreased by 1, the element at index is decreased by 2, and the element at index+1 is decreased by 1.
#Overall this is what the function does:The function accepts a list of integers `array` and an integer `index` (where 2 <= index <= len(array) - 1). It returns a new list of integers where the element at index-1 is decreased by 1, the element at index is decreased by 2, and the element at index+1 is decreased by 1. After the function concludes, the original list `array` remains unchanged, and the returned list reflects the specified decrements at the given indices.

#State of the program right berfore the function call: arrayForSuccess is a list of integers representing the current state of Rudolf's array after applying the operations.
def func_2(arrayForSuccess):
    for x in arrayForSuccess:
        if x != 0:
            return False
        
    #State: Output State: The function has returned False because one of the elements in `arrayForSuccess` was not equal to 0 during the loop's execution.
    #
    #Explanation: Given the conditions provided, the loop will continue to iterate through each element in `arrayForSuccess` as long as `x` is not equal to 0. Since the loop executed up to the third iteration, it means that the first two elements were equal to 0 (otherwise, the function would have returned False earlier). However, the third element was not equal to 0, which caused the function to return False immediately. Therefore, the final state of the function is that it has returned False due to finding a non-zero element in the list.
    return True
    #The program returns True
#Overall this is what the function does:The function `func_2` accepts a list of integers named `arrayForSuccess`. It checks each element in the list; if any element is not equal to zero, the function returns `False`. If all elements are zero, the function returns `True`. There are four possible outcomes: the function returns `False` if any non-zero element is found, and it returns `True` only if all elements are zero.

#State of the program right berfore the function call: inputarray is a list of integers with at least 3 elements, where each element is in the range [0, 10^9].
def func_3(inputarray):
    if func_2(inputarray) :
        answers.append('YES')
        return
        #The program returns 'YES'
    #State: inputarray is a list of integers with at least 3 elements, where each element is in the range [0, 10^9], and the function func_2(inputarray) returns False
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
        
    #State: Output State: `loop_counter` is 100, `length` is greater than 1, `elementIndex` is equal to `length - 1`, `highestNumber` is the maximum value found in the array `inputarray` from index 1 to `length - 1`, `highestIndex` is the index of the highest number in the array, `newArray` is the result of `func_1(inputarray, highestIndex)`, and `func_2(newArray)` has been called but did not return 'YES'. 
    #
    #Explanation: After the loop executes all its iterations (i.e., `loop_counter` reaches 100), the loop condition (`loop_counter != 100`) becomes false, terminating the loop. At this point, `loop_counter` will be 100. The loop processes each possible `elementIndex` from 1 to `length - 2` during its iterations, ensuring that `highestNumber` and `highestIndex` are updated appropriately. The final state of `elementIndex` will be `length - 1`, as it checks up to the second last element in the array. The value of `highestNumber` will be the maximum value found in the array from index 1 to `length - 1`, and `highestIndex` will be the index of this maximum value. `newArray` will be the result of `func_1(inputarray, highestIndex)` after the last iteration, and `func_2(newArray)` has been evaluated but did not return 'YES', otherwise the loop would have terminated earlier.
    answers.append('NO')
#Overall this is what the function does:The function `func_3` accepts a list of integers `inputarray` with at least 3 elements, where each element is in the range [0, 10^9]. It first checks if `func_2(inputarray)` returns `True`. If so, it appends 'YES' to the `answers` list and returns. If not, it iterates up to 100 times, finding the highest number in the array excluding the first and last elements, creating a new array based on this highest number, and checking if `func_2(newArray)` returns `True`. If `func_2(newArray)` returns `True` at any point, it appends 'YES' to the `answers` list and returns. If the loop completes without finding such a case, it appends 'NO' to the `answers` list and returns. The function can return 'YES', 'NO', or `None` based on the conditions met during its execution.


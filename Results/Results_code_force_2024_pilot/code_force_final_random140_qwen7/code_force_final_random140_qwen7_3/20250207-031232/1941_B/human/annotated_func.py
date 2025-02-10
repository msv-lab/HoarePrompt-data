#State of the program right berfore the function call: array is a list of integers with at least 3 elements, index is an integer such that 2 <= index <= len(array) - 1.
def func_1(array, index):
    array[index - 1] = array[index - 1] - 1
    array[index] = array[index] - 2
    array[index + 1] = array[index + 1] - 1
    return array
    #The program returns a list of integers where the element at index-1 is decreased by 1, the element at index is decreased by 2, and the element at index+1 is decreased by 1 from the original array.
#Overall this is what the function does:The function accepts a list of integers `array` and an integer `index`. It returns a new list where the element at position `index-1` is decreased by 1, the element at position `index` is decreased by 2, and the element at position `index+1` is decreased by 1, while all other elements remain unchanged.

#State of the program right berfore the function call: arrayForSuccess is a list of integers representing the array after applying the operations.
def func_2(arrayForSuccess):
    for x in arrayForSuccess:
        if x != 0:
            return False
        
    #State: Output State: The function has returned False.
    #
    #Explanation: Given the conditions provided, the loop will continue to iterate as long as `x` is not equal to 0. Since the output state after the loop executes 3 times indicates that `x` is an integer that is not equal to 0 and the function returns False, it means that the loop must have encountered at least one non-zero value in `arrayForSuccess`. Therefore, after all iterations of the loop have finished, the function has returned False.
    return True
    #The program returns False
#Overall this is what the function does:The function `func_2` accepts a list of integers named `arrayForSuccess`. It iterates through each element in the list. If any element is not equal to zero, the function immediately returns `False`. If all elements are zero, the function also returns `False`. In all cases, the function guarantees to return `False`.

#State of the program right berfore the function call: inputarray is a list of integers, where the length of the list is n (3 ≤ n ≤ 2 \cdot 10^5), and each element a_j (0 ≤ a_j ≤ 10^9).
def func_3(inputarray):
    if func_2(inputarray) :
        answers.append('YES')
        return
        #The program returns 'YES'
    #State: inputarray is a list of integers, where the length of the list is n (3 ≤ n ≤ 2 \cdot 10^5), and each element a_j (0 ≤ a_j ≤ 10^9). The function func_2(inputarray) returns False
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
        
    #State: Output State: `elementIndex` is equal to `length - 2`, `highestIndex` is the index where the highest value in `inputarray` was found during the loop's execution, `highestNumber` is the highest value itself, `newArray` is the result of calling `func_1(inputarray, highestIndex)` with `inputarray` and `highestIndex` as arguments, `loop_counter` is 100, and `func_2(newArray)` has been called 99 times and returned `False` each time.
    #
    #This means that the loop has executed 100 times, checking each element in the array except the first and last elements. The `loop_counter` is now 100, and since the condition `loop_counter != 100` is no longer true, the loop will terminate. The `elementIndex` is set to `length - 2` because the loop increments `loop_counter` before checking the condition, so it checks up to the second-to-last element. The `highestIndex` and `highestNumber` are determined based on the maximum value found in the array during the loop's execution. The `newArray` is the result of the last call to `func_1(inputarray, highestIndex)`. Since `func_2(newArray)` has been called 99 times and returned `False` each time, it will not append 'YES' to `answers` and the loop will exit without appending 'NO' either, meaning `answers` remains unchanged.
    answers.append('NO')
#Overall this is what the function does:The function `func_3` accepts a list of integers `inputarray` and may return 'YES' if certain conditions are met during its execution. If these conditions are not met, the function does not return any value. Specifically, the function iterates through the list, identifies the highest number and its index, and modifies the list based on this information. It then checks if the modified list satisfies a condition using `func_2`. If `func_2` returns 'YES', the function appends 'YES' to the `answers` list and returns. If the loop completes 100 iterations without finding a suitable modification, the function appends 'NO' to the `answers` list and returns. If `func_2` never returns 'YES' within the loop, the function also appends 'NO' to the `answers` list and returns. In cases where the function does not return a value, it indicates that none of the conditions were satisfied.


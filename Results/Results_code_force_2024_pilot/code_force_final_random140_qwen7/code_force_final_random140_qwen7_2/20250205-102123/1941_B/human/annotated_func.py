#State of the program right berfore the function call: array is a list of integers with length n, index is an integer such that 2 <= index <= n - 1, and the elements of the array are non-negative integers.
def func_1(array, index):
    array[index - 1] = array[index - 1] - 1
    array[index] = array[index] - 2
    array[index + 1] = array[index + 1] - 1
    return array
    #The program returns a list of integers where each element is the same as the original element minus 3, except for the element at position index which remains unchanged.
#Overall this is what the function does:The function accepts a list of non-negative integers `array` and an integer `index`. It returns a new list where each element is reduced by 3, except for the element at position `index`, which remains unchanged.

#State of the program right berfore the function call: arrayForSuccess is a list of integers representing the current state of Rudolf's array after performing the operations.
def func_2(arrayForSuccess):
    for x in arrayForSuccess:
        if x != 0:
            return False
        
    #State: Output State: `arrayForSuccess` is a list of integers where all elements are zero.
    #
    #This is because the loop continues to execute as long as there is at least one non-zero element in `arrayForSuccess`. Once the loop has executed three times and the second element is confirmed to be zero, it means all elements in the list must be zero for the loop to continue without returning False. Since the loop does not modify the list but only checks its elements, and it keeps running until it finds a non-zero element which never happens, all elements must be zero by the end of the loop.
    return True
    #The program returns True
#Overall this is what the function does:The function `func_2` accepts a list of integers `arrayForSuccess` and returns `True` if all elements in the list are zero. Otherwise, it returns `False`.

#State of the program right berfore the function call: inputarray is a list of integers, where the length of the list is n (3 ≤ n ≤ 2 \cdot 10^5), and each element a_j (0 ≤ a_j ≤ 10^9).
def func_3(inputarray):
    if func_2(inputarray) :
        answers.append('YES')
        return
        #The program does not return any value
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
        
    #State: Output State: `elementIndex` is 98, `length` is 100, `highestIndex` is 99, `highestNumber` is the maximum value found in the subarray from `inputarray[1]` to `inputarray[99]`, `loop_counter` is 100, `newArray` is the result of calling `func_1(inputarray, 99)`.
    #
    #Explanation: After the loop completes all its iterations, `loop_counter` will reach 100, which is the condition that breaks the while loop. By the last iteration, `elementIndex` will still be 98 because the loop increments `loop_counter` but does not change `elementIndex`. The `length` of `inputarray` remains 100 as it is not modified within the loop. `highestIndex` will be the last valid index checked, which is 99, and `highestNumber` will be the maximum value found in the subarray from `inputarray[1]` to `inputarray[99]`. `newArray` will be the result of the last call to `func_1(inputarray, 99)`.
    answers.append('NO')
#Overall this is what the function does:The function accepts a list of integers and processes it without returning any value. It checks if certain conditions are met using `func_2` and `func_1`. If these conditions are satisfied, it appends 'YES' to the `answers` list. If not, it finds the highest number in a specific subarray of the input list, creates a new array based on this highest number, and repeats the check. If after 100 iterations, the conditions are still not met, it appends 'NO' to the `answers` list.


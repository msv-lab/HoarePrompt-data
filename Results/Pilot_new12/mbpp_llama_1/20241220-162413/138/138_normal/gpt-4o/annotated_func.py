#State of the program right berfore the function call: arr is a list and element is any type of object that can be compared with elements in arr.
def func_1(arr, element):
    for (index, value) in enumerate(arr):
        if value == element:
            return True, index
        
    #State of the program after the  for loop has been executed: To determine the output state after all iterations of the loop have finished, let's analyze the loop's behavior based on the provided code and output states for the first few iterations.
    #
    #1. **Loop Execution**: The loop iterates over the list `arr` using `enumerate`, which provides both the index and the value of each element in `arr`.
    #
    #2. **Conditional Return**: Inside the loop, there's a conditional check `if value == element`. If this condition is true, the function immediately returns `True` along with the index of the matching element.
    #
    #3. **Output States Analysis**:
    #   - After the loop executes 1 time, `arr` must have at least 1 element, and `value` is not equal to `element`, or the loop would have returned.
    #   - After the loop executes 2 times, `arr` must have at least 2 elements. If `value` equals `element` at any point, the function returns; otherwise, it continues.
    #   - After the loop executes 3 times, similar logic applies, with the function returning if a match is found.
    #
    #**Determining the Final Output State**:
    #
    #- **If `element` is found in `arr`**: The loop will return `True` and the index of the first occurrence of `element` in `arr`. In this case, the loop does not complete all iterations.
    #  
    #- **If `element` is not found in `arr`**: The loop will iterate over all elements in `arr` without finding a match. In this scenario, the function does not explicitly return a value, implying it returns `None` by default in many programming languages. The state of `arr`, `element`, `index`, and `value` after the loop would reflect the last iteration: `index` would be the last index of `arr`, `value` would be the last element of `arr`, and `arr` and `element` would retain their original values since the loop does not modify them.
    #
    #Given this analysis, the output state after all iterations of the loop have finished (or not, in the case of an early return) can be summarized as follows:
    #
    #- If `element` is found in `arr`, the function returns `True` and the index of `element`.
    #- If `element` is not found in `arr`, the function implicitly returns `None`, with `index` being the last index of `arr`, `value` being the last element of `arr`, and `arr` and `element` remaining unchanged.
    #
    #However, the task requires focusing on the state of variables after the loop, considering the original task's format for the answer.
    #
    #**Output State: `arr` is a list, `element` is any type of object, if `element` is in `arr`, the function returns True and the index of `element`; otherwise, the function returns None, with `index` being the last index of `arr` and `value` being the last element of `arr`.**
    return False, -1
    #The program returns False, indicating that the element was not found, and -1, representing an invalid index, signifying that the element was not located in the list.
#Overall this is what the function does:The function `func_1` searches for an `element` in a given list `arr` and returns a tuple containing a boolean value and an index. If the `element` is found, the function returns `True` along with the index of the `element` in the list. If the `element` is not found, the function returns `False` and `-1`. The function iterates over the list using `enumerate` to access both the index and value of each element, and it stops as soon as it finds a match, making it efficient for large lists where the target element is near the beginning. The function does not modify the original list or the `element` being searched. Potential edge cases include an empty list, a list with duplicate elements (where it returns the index of the first occurrence), and searching for `None` or other special values, all of which are handled by the function's return values. If the list is empty, the function will return `False` and `-1` without throwing an error, indicating that the `element` was not found.


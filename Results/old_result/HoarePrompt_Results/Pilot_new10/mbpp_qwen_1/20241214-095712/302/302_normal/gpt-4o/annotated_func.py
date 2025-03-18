#State of the program right berfore the function call: arr is a list of integers sorted in non-decreasing order, and target is an integer.
def func_1(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            result = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        
    #State of the program after the loop has been executed: `arr` is a list of integers sorted in non-decreasing order, `target` is an integer, `result` is the index of `target` in `arr` if found, otherwise it remains -1, `low` is 0, `high` is -1, `mid` is -1
    return result
    #The program returns -1 since `result` remains -1 as no search process has been conducted and `target` might not be in `arr`
#Overall this is what the function does:Let's analyze the provided annotated code step by step:

1. **Initial State**: The function `func_1` accepts two parameters: `arr`, a list of integers sorted in non-decreasing order, and `target`, an integer.
2. **Variable Initialization**: The variables `low` and `high` are initialized to 0 and `len(arr) - 1`, respectively. The variable `result` is initialized to -1.
3. **Binary Search Loop**:
   - The loop continues as long as `low` is less than or equal to `high`.
   - Inside the loop, the middle index `mid` is calculated as `(low + high) // 2`.
   - If `arr[mid]` equals `target`, `result` is set to `mid` and `high` is set to `mid - 1` to search in the left half.
   - If `arr[mid]` is less than `target`, `low` is set to `mid + 1` to search in the right half.
   - If `arr[mid]` is greater than `target`, `high` is set to `mid - 1` to search in the left half.
4. **Post-loop State**: After the loop, `result` contains the index of `target` if found, otherwise it remains -1. `low` and `high` are set to 0 and -1, respectively, and `mid` is set to -1.
5. **Return Statement**: The function returns `result`.

From the code, we can observe that the function performs a binary search on the sorted list `arr` to find the index of `target`. If the target is found, it returns the index; otherwise, it returns -1.

**Analyze Potential Edge Cases**:
- **Empty List**: If `arr` is empty, `low` will never be less than or equal to `high`, so the loop will never run, and `result` will remain -1.
- **Single Element**: If `arr` has only one element and it matches `target`, the function will return the index of that element.
- **Target Not Found**: If `target` is not present in `arr`, the function will return -1.

Given the return postconditions and the actual code, the functionality of the function is correctly described in the initial annotation. However, it is important to note that the function returns -1 if the target is not found, regardless of whether a search process was conducted or not.

**Functionality: **The function `func_1` accepts a list `arr` of integers sorted in non-decreasing order and an integer `target`. It performs a binary search to find the index of `target` in `arr`. If the target is found, it returns the index; otherwise, it returns -1.


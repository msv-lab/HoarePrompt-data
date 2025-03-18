#State of the program right berfore the function call: arr is a list of integers where each integer a_i satisfies 1 ≤ a_i ≤ n, and the length of arr, denoted as n, satisfies 1 ≤ n ≤ 2 · 10^5. The function is called once for each test case, and the total number of test cases, t, satisfies 1 ≤ t ≤ 10^4. The sum of n across all test cases does not exceed 2 · 10^5.
def func_1(arr):
    i = 0
    j = len(arr) - 1
    while i <= j:
        if arr[i] == arr[j]:
            i += 1
            j -= 1
        else:
            break
        
    #State: i and j are such that either i > j or arr[i] != arr[j].
    if (i > j) :
        return 0
        #The program returns 0
    #State: i and j are such that i is not greater than j, and either i > j or arr[i] != arr[j] is still true, implying that arr[i] != arr[j] must be the case.
    while arr[i] == arr[i + 1]:
        i += 1
        
    #State: To determine the final output state after the loop has finished executing, we need to understand the loop's behavior. The loop increments `i` as long as `arr[i]` is equal to `arr[i + 1]`. The loop stops when `arr[i]` is no longer equal to `arr[i + 1]`.
    #
    #Given the initial state and the output states after the first 3 iterations, we can infer that:
    #- `i` is incremented by 3, meaning that `arr[i]` was equal to `arr[i + 1]`, `arr[i + 1]` was equal to `arr[i + 2]`, and `arr[i + 2]` was equal to `arr[i + 3]` at the start of the 3rd iteration.
    #- The loop stops when `arr[i + 3]` is not equal to `arr[i + 4]`.
    #
    #Thus, after the loop finishes, `i` will be incremented to the position where `arr[i]` is no longer equal to `arr[i + 1]`. `j` remains unchanged throughout the loop.
    #
    #**Output State: i is incremented to the position where arr[i] is no longer equal to arr[i + 1], and j is unchanged.**
    #
    #In simpler terms, `i` will point to the first element in the array that is not equal to the next element, and `j` will stay the same as it was initially.
    if (j != len(arr) - 1) :
        return j - i + 1
        #The program returns `j - i + 1`, where `i` is the position in the array `arr` where `arr[i]` is no longer equal to `arr[i + 1]`, and `j` is unchanged and not equal to the last index of `arr`.
    #State: `i` is incremented to the position where `arr[i]` is no longer equal to `arr[i + 1]`, and `j` is unchanged. Additionally, `j` is equal to `len(arr) - 1`.
    return j - i
    #The program returns the difference between `len(arr) - 1` and the position `i` where `arr[i]` is no longer equal to `arr[i + 1]`.
#Overall this is what the function does:The function `func_1` takes a list of integers `arr` as input and returns 0 if all elements in `arr` are the same. Otherwise, it returns the length of the longest contiguous subarray starting from the beginning or ending at the end where all elements are the same.


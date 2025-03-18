#State of the program right berfore the function call: arr is a list of integers where the length of the list is n (1 <= n <= 2 * 10^5), and each element in the list is an integer between 1 and n inclusive. The sum of all lengths n across all test cases does not exceed 2 * 10^5.
def func_1(arr):
    i = 0
    n = len(arr)
    j = len(arr) - 1
    while i < len(arr) - 1 and arr[i] == arr[i + 1]:
        i += 1
        
    #State: i is the index just after the last consecutive duplicate element in arr, or equal to len(arr) if there are no consecutive duplicates.
    while j > 0 and arr[j] == arr[j - 1]:
        j -= 1
        
    #State: Output State: j is the index just after the last consecutive duplicate element in arr, or equal to 0 if there are no consecutive duplicates.
    #
    #Explanation: The given loop decrements `j` as long as `j` is greater than 0 and the current element `arr[j]` is equal to the previous element `arr[j-1]`. This means it will continue to decrement `j` until it either finds a non-duplicate element or reaches the start of the array. Therefore, after the loop finishes executing, `j` will be the index just after the last consecutive duplicate element in `arr`, or 0 if there are no consecutive duplicates.
    if (arr[0] == arr[-1]) :
        return max(j - i - 1, 0)
        #The program returns the maximum value between j - i - 1 and 0, where j is the index just after the last consecutive duplicate element in arr, or 0 if there are no consecutive duplicates, and i is 0 since arr[0] is equal to arr[-1]
    #State: `j` is the index just after the last consecutive duplicate element in `arr`, or equal to 0 if there are no consecutive duplicates, and `arr[0]` is not equal to `arr[-1]`
    return max(min(n - i - 1, j), 0)
    #The program returns the maximum value between the minimum of (n - i - 1) and j, ensuring the result is at least 0
#Overall this is what the function does:The function `func_1` accepts a list `arr` of integers and returns the maximum value between `j - i - 1` and 0, where `j` is the index just after the last consecutive duplicate element in `arr`, or 0 if there are no consecutive duplicates, and `i` is 0 since `arr[0]` is equal to `arr[-1]`. Alternatively, it returns the maximum value between the minimum of (n - i - 1) and `j`, ensuring the result is at least 0.


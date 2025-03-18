#State of the program right berfore the function call: arr is a list of integers where the length of the list is n (1 <= n <= 2 * 10^5), and each element a_i satisfies 1 <= a_i <= n.
def func_1(arr):
    i = 0
    n = len(arr)
    j = len(arr) - 1
    while i < len(arr) - 1 and arr[i] == arr[i + 1]:
        i += 1
        
    #State: Output State: `i` is equal to the length of `arr`, `j` is the length of `arr` - 1, and all elements from `arr[0]` to `arr[i-1]` are identical.
    #
    #This means that the loop continues to increment `i` as long as the current element is equal to the next one, effectively skipping over consecutive duplicates. Once `i` reaches a point where `arr[i]` is no longer equal to `arr[i + 1]`, or it reaches the second last element of the array, the loop stops. At the end, `i` will be at the position right after the last group of consecutive duplicates, or at the end of the array if there were no duplicates. The value of `j` remains unchanged as it was not affected by the loop.
    while j > 0 and arr[j] == arr[j - 1]:
        j -= 1
        
    #State: Output State: `i` is equal to the length of `arr`, `j` is 0, and all elements from `arr[0]` to `arr[i-1]` are identical.
    #
    #Explanation: After the loop has executed all its iterations, `j` will eventually reach 0 because the loop decrements `j` by 1 each time it finds that `arr[j]` is equal to `arr[j - 1]`. Since the loop stops when `j` is no longer greater than 0, `j` will be 0 at the end. Also, since the loop only increments `i` when it skips over consecutive duplicates, `i` will always be equal to the length of `arr` because the condition to increment `i` is never met (as the loop only affects `j`). All elements from `arr[0]` to `arr[i-1]` (which is the entire array) are identical due to the initial condition and the nature of the loop.
    if (arr[0] == arr[-1]) :
        return max(j - i - 1, 0)
        #The program returns the maximum value between 0 and the difference between j (which is 0) and i (which is the length of arr), minus 1.
    #State: `i` is equal to the length of `arr`, `j` is 0, and all elements from `arr[0]` to `arr[i-1]` (which is the entire array) are not identical.
    return max(min(n - i - 1, j), 0)
    #The program returns the maximum value between the minimum of (n - i - 1 and j) and 0, where n is the length of the array arr, i is the length of arr, and j is 0.
#Overall this is what the function does:The function accepts a list of integers `arr` and returns a non-negative integer. It first processes the list to find the position `i` right after the last group of consecutive duplicates and sets `j` to the last index of the list. If all elements in the list are identical, it returns the maximum value between 0 and the difference between `j` (which is 0) and `i` (which is the length of `arr`), minus 1. Otherwise, it returns the maximum value between the minimum of (`n - i - 1` and `j`) and 0, where `n` is the length of the array `arr`.


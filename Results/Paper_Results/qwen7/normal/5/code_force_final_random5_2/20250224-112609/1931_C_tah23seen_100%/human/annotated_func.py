#State of the program right berfore the function call: arr is a list of integers where the length of the list is n (1 <= n <= 2 * 10^5), and each element a_i satisfies 1 <= a_i <= n.
def func_1(arr):
    i = 0
    n = len(arr)
    j = len(arr) - 1
    while i < len(arr) - 1 and arr[i] == arr[i + 1]:
        i += 1
        
    #State: Output State: `i` is the length of `arr`, `j` is the length of `arr` - 1, and all elements from `arr[0]` to `arr[len(arr)-2]` must be equal.
    #
    #Explanation: The loop continues to increment `i` as long as `i` is less than `len(arr) - 1` and `arr[i]` is equal to `arr[i + 1]`. This means that the loop will keep running until it finds a pair of elements that are not equal or until it reaches the second last element of the array. Therefore, after the loop completes, `i` will be set to the index right after the last pair of equal consecutive elements, effectively making `i` equal to the length of the array. The variable `j` remains unchanged as it was not affected by the loop. All elements from `arr[0]` to `arr[len(arr)-2]` must be equal for the loop to terminate in this manner.
    while j > 0 and arr[j] == arr[j - 1]:
        j -= 1
        
    #State: `i` is the length of `arr`, `j` is 0, and all elements from `arr[0]` to `arr[len(arr)-2]` are equal.
    if (arr[0] == arr[-1]) :
        return max(j - i - 1, 0)
        #The program returns the maximum value between j - i - 1 and 0, where j is 0 and i is the length of arr.
    #State: `i` is the length of `arr`, `j` is 0, and not all elements from `arr[0]` to `arr[len(arr)-2]` are equal.
    return max(min(n - i - 1, j), 0)
    #The program returns the maximum value between the minimum of (n - i - 1) and j, which is 0, given that not all elements from arr[0] to arr[len(arr)-2] are equal.
#Overall this is what the function does:The function accepts a list of integers `arr` and returns a non-negative integer. It first checks if all elements from the start to the second last element of the array are equal. If they are, it returns the maximum value between `j - i - 1` and 0, where `j` is 0 and `i` is the length of `arr`. If not all elements are equal, it returns the maximum value between the minimum of `(n - i - 1)` and `j`, which is 0, where `n` is the length of `arr`.


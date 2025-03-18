#State of the program right berfore the function call: arr is a list of integers where each integer is between 1 and n (inclusive), and n is the length of the list arr. The function is called for each test case, and the total number of elements across all test cases does not exceed 2 \cdot 10^5.
def func_1(arr):
    i = 0
    n = len(arr)
    j = len(arr) - 1
    while i < len(arr) - 1 and arr[i] == arr[i + 1]:
        i += 1
        
    #State: `i` is the index of the first element in `arr` that is not equal to the element immediately following it, or `len(arr) - 1` if all elements are the same; `j` is `n - 1`.
    while j > 0 and arr[j] == arr[j - 1]:
        j -= 1
        
    #State: `j` is the index of the last element in the array that is different from the element immediately preceding it, or 0 if all elements from `j` to the start of the array are the same.
    if (arr[0] == arr[-1]) :
        return max(j - i - 1, 0)
        #The program returns the maximum value between `j - i - 1` and 0.
    #State: `j` is the index of the last element in the array that is different from the element immediately preceding it, or 0 if all elements from `j` to the start of the array are the same. The first element of the array is not equal to the last element of the array.
    return max(min(n - i - 1, j), 0)
    #The program returns the maximum of 0 and the minimum of (n - i - 1) and j.
#Overall this is what the function does:The function `func_1` takes a list of integers `arr` as input and returns the length of the longest segment of the list that does not include the first and last elements if they are the same, or the length of the longest segment that does not include the first or last element if they are different. The function ensures that the returned value is at least 0.


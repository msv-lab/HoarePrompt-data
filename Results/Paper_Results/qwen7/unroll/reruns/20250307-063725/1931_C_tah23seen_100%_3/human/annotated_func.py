#State of the program right berfore the function call: arr is a list of integers where the length of the list is n (1 <= n <= 2 * 10^5), and each element in the list is an integer between 1 and n inclusive.
def func_1(arr):
    i = 0
    n = len(arr)
    j = len(arr) - 1
    while i < len(arr) - 1 and arr[i] == arr[i + 1]:
        i += 1
        
    #State: i is the index where the first pair of unequal elements is found or len(arr) - 1 if all elements are equal.
    while j > 0 and arr[j] == arr[j - 1]:
        j -= 1
        
    #State: j is the index of the last element that is different from the next one, or 0 if all elements are the same.
    if (arr[0] == arr[-1]) :
        return max(j - i - 1, 0)
        #The program returns the maximum value between (j - i - 1) and 0, where `j` is the index of the last element that is different from the next one, or 0 if all elements are the same, and `i` is the index of the first element of the array `arr` which is also its last element since `arr[0] == arr[-1]`.
    #State: j is the index of the last element that is different from the next one, or 0 if all elements are the same. The first element of `arr` is not equal to the last element of `arr`.
    return max(min(n - i - 1, j), 0)
    #The program returns the maximum value between the minimum of (n - j - 1) and (j), where n is the length of the array `arr`.
#Overall this is what the function does:The function accepts a list of integers `arr` and returns the maximum value between two possible calculations. In the first case, it calculates the maximum value between (j - i - 1) and 0, where `j` is the index of the last element that is different from the next one, or 0 if all elements are the same, and `i` is the index of the first element of the array `arr` which is also its last element since `arr[0] == arr[-1]`. In the second case, it returns the maximum value between the minimum of (n - j - 1) and (j), where `n` is the length of the array `arr`.


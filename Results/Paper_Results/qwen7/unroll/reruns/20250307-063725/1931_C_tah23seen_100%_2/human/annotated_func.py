#State of the program right berfore the function call: arr is a list of integers where the length of the list is n (1 <= n <= 2 * 10^5), and each element a_i satisfies 1 <= a_i <= n.
def func_1(arr):
    i = 0
    n = len(arr)
    j = len(arr) - 1
    while i < len(arr) - 1 and arr[i] == arr[i + 1]:
        i += 1
        
    #State: i is the index where arr[i] != arr[i + 1] or len(arr) - 1 if such index does not exist.
    while j > 0 and arr[j] == arr[j - 1]:
        j -= 1
        
    #State: Output State: j is the index pointing to the first element from the end of the array that is different from its predecessor, or 0 if all elements in the array are the same.
    #
    #Explanation: The loop decrements `j` as long as `j` is greater than 0 and the current element `arr[j]` is equal to the previous element `arr[j-1]`. This means that `j` will keep moving towards the start of the array until it either reaches the beginning (index 0) or finds an element that is different from its predecessor. At the end of the loop, `j` will point to the first element from the end of the array that is different from its predecessor, or it will be at index 0 if all elements in the array are the same.
    if (arr[0] == arr[-1]) :
        return max(j - i - 1, 0)
        #The program returns 0
    #State: `j` is the index pointing to the first element from the end of the array that is different from its predecessor, or 0 if all elements in the array are the same. Additionally, the first element `arr[0]` is not equal to the last element `arr[-1]`.
    return max(min(n - i - 1, j), 0)
    #The program returns the maximum value between the minimum of (n - i - 1) and j, ensuring the result is at least 0. Here, n is the length of the array, i is the index pointing to the first element from the end of the array that is different from its predecessor, or 0 if all elements in the array are the same, and j is also 0 since the first element arr[0] is not equal to the last element arr[-1].
#Overall this is what the function does:The function accepts a list of integers `arr` and returns an integer. It first finds the index `i` from the start of the array where the current element differs from the next one, or 0 if all elements are the same. Then, it finds the index `j` from the end of the array where the current element differs from the previous one, or 0 if all elements are the same. If the first and last elements are the same, it returns 0. Otherwise, it returns the maximum value between the minimum of `(n - i - 1)` and `j`, ensuring the result is at least 0. Here, `n` is the length of the array.


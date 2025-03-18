#State of the program right berfore the function call: arr is a list of integers where each integer a_i satisfies 1 <= a_i <= n, and n is the length of the list arr. The function is called multiple times for different test cases, with the total number of elements across all test cases not exceeding 2 * 10^5.
def func_1(arr):
    i = 0
    n = len(arr)
    j = len(arr) - 1
    while i < len(arr) - 1 and arr[i] == arr[i + 1]:
        i += 1
        
    #State: `i` is the first index where `arr[i] != arr[i + 1]` or `len(arr) - 1` if all elements are equal; `j` is `n - 1`.
    while j > 0 and arr[j] == arr[j - 1]:
        j -= 1
        
    #State: `i` is the first index where `arr[i] != arr[i + 1]` or `len(arr) - 1` if all elements are equal; `j` is the first index from the end where `arr[j] != arr[j - 1]` or 0 if all elements are equal from the end to the beginning.
    if (arr[0] == arr[-1]) :
        return max(j - i - 1, 0)
        #The program returns the number of elements between the first index where the element differs from its next neighbor and the first index from the end where the element differs from its previous neighbor, exclusive, or 0 if all elements are equal.
    #State: `i` is the first index where `arr[i] != arr[i + 1]` or `len(arr) - 1` if all elements are equal; `j` is the first index from the end where `arr[j] != arr[j - 1]` or 0 if all elements are equal from the end to the beginning; the first element of `arr` is not equal to the last element of `arr`
    return max(min(n - i - 1, j), 0)
    #The program returns the maximum of the minimum between the number of elements between `i` and the end of the array (exclusive) and the number of elements from the start of the array to `j` (exclusive).
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` where each integer is between 1 and the length of the list. It returns the number of elements between the first index where the element differs from its next neighbor and the first index from the end where the element differs from its previous neighbor, exclusive. If all elements are equal, it returns 0. If not all elements are equal, it returns the maximum of the minimum between the number of elements from the first differing element to the end of the list (exclusive) and the number of elements from the start of the list to the first differing element from the end (exclusive).


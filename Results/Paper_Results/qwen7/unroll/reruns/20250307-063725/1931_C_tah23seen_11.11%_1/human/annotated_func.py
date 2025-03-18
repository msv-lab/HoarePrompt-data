#State of the program right berfore the function call: arr is a list of integers where the length of the list is n (1 <= n <= 2 * 10^5), and each element a_i satisfies 1 <= a_i <= n.
def func_1(arr):
    i = 0
    j = len(arr) - 1
    while i <= j:
        if arr[i] == arr[j]:
            i += 1
            j -= 1
        else:
            break
        
    #State: i is greater than j.
    if (i > j) :
        return 0
        #The program returns 0
    #State: i is greater than j
    while arr[i] == arr[i + 1]:
        i += 1
        
    #State: Output State: i points to an index where arr[i] is no longer equal to arr[i + 1].
    #
    #Explanation: The loop continues as long as the current element `arr[i]` is equal to the next element `arr[i + 1]`. Each iteration of the loop increments `i` by 1. This process continues until `arr[i]` is no longer equal to `arr[i + 1]`, at which point the loop terminates. Therefore, after the loop finishes executing, `i` will be pointing to an index where the condition `arr[i] == arr[i + 1]` is false.
    if (j != len(arr) - 1) :
        return j - i + 1
        #The program returns the difference between index `j` and index `i` plus one, which represents the length of the subarray starting from index `i` to index `j` where each element is not equal to its next element.
    #State: `i` points to an index where `arr[i]` is no longer equal to `arr[i + 1]`, and `j` is equal to the length of `arr` minus one
    return j - i
    #The program returns the difference between the length of array `arr` minus one and the index `i` where `arr[i]` is no longer equal to `arr[i + 1]`.
#Overall this is what the function does:The function accepts a list of integers `arr` and returns either 0, the length of a subarray where each element is not equal to its next element, or the difference between the length of `arr` minus one and the index `i` where `arr[i]` is no longer equal to `arr[i + 1]`.


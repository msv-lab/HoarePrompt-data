#State of the program right berfore the function call: arr is a list of integers where the length of the list is n (1 <= n <= 2 * 10^5), and each element in the list is an integer between 1 and n inclusive.
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
    #Explanation: The loop continues as long as the element at index `i` is equal to the element at index `i + 1`. Each iteration of the loop increments `i` by 1. This process continues until it finds an index `i` where `arr[i]` is not equal to `arr[i + 1]`, or if there are no more elements to compare (i.e., `i + 1` exceeds the array length). At this point, the loop terminates, and `i` will point to the last index where consecutive elements were found to be equal.
    if (j != len(arr) - 1) :
        return j - i + 1
        #The program returns the difference between j and i plus 1, where j is not equal to the length of arr minus 1 and i points to an index where arr[i] is no longer equal to arr[i + 1]
    #State: `i` points to an index where `arr[i]` is no longer equal to `arr[i + 1]`, and `j` equals the length of the array `arr`.
    return j - i
    #The program returns the difference between the length of the array `arr` and the index `i` where `arr[i]` is no longer equal to `arr[i + 1]`.
#Overall this is what the function does:The function `func_1` accepts a list `arr` of integers and returns either 0, the difference between `j` and `i` plus 1 under certain conditions, or the difference between the length of the array and the index `i` where the condition is met. Specifically, it checks for consecutive equal elements in the list and calculates the length of the longest sequence of such elements. If no such sequence exists, it returns 0. Otherwise, it returns the length of the longest sequence or the remaining part of the list after the sequence.


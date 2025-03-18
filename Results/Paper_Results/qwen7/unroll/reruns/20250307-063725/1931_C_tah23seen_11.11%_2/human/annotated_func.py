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
        
    #State: Output State: i points to the first element in arr that is different from the previous element or is out of bounds.
    #
    #Explanation: The loop continues to increment `i` as long as the current element `arr[i]` is equal to the next element `arr[i + 1]`. This means that `i` will keep increasing until it reaches an index where `arr[i]` is not equal to `arr[i + 1]`, or until `i + 1` exceeds the length of the array `arr`. After the loop finishes, `i` will point to either the first element that is different from its predecessor or it will be out of bounds if all elements were identical.
    if (j != len(arr) - 1) :
        return j - i + 1
        #The program returns the number of elements from index `i` to index `j-1` in the list `arr`
    #State: `i` points to the first element in `arr` that is different from the previous element or is out of bounds, and `j` is equal to the length of `arr` - 1
    return j - i
    #The program returns the difference between the length of list 'arr' minus 1 and the index 'i' that points to the first element in 'arr' which is different from the previous element or is out of bounds.
#Overall this is what the function does:The function accepts a list of integers `arr` and returns either 0, the count of elements from index `i` to index `j-1` in the list `arr`, or the difference between the length of list `arr` minus 1 and the index `i` pointing to the first element in `arr` which is different from the previous element or is out of bounds.


#State of the program right berfore the function call: arr is a list of integers where each integer a_i satisfies 1 <= a_i <= n, and n is the length of the list arr. The function is called once for each test case, and the total number of elements across all test cases does not exceed 2 * 10^5.
def func_1(arr):
    i = 0
    j = len(arr) - 1
    while i <= j:
        if arr[i] == arr[j]:
            i += 1
            j -= 1
        else:
            break
        
    #State: 
    if (i > j) :
        return 0
        #The program returns 0
    #State: `i` and `j` are integers, and `i` is less than or equal to `j`
    while arr[i] == arr[i + 1]:
        i += 1
        
    #State: `i` is the smallest index such that `arr[i]` is not equal to `arr[i + 1]`, or `i` is equal to `j` if all elements from `arr[i]` to `arr[j]` are the same.
    if (j != len(arr) - 1) :
        return j - i + 1
        #The program returns the length of the segment starting from index `i` to `j` inclusive, which is `j - i + 1`.
    #State: `i` is the smallest index such that `arr[i]` is not equal to `arr[i + 1]`, or `i` is equal to `j` if all elements from `arr[i]` to `arr[j]` are the same. Additionally, `j` is equal to `len(arr) - 1`.
    return j - i
    #The program returns the length of the array `arr` minus the smallest index `i` such that `arr[i]` is not equal to `arr[i + 1]`, or it returns 0 if all elements from `arr[i]` to `arr[j]` are the same.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` where each integer is between 1 and the length of the list `arr`. It returns 0 if the list is a palindrome or if all elements from the start to the end are the same. Otherwise, it returns the length of the longest segment from the start or end of the list where all elements are the same.


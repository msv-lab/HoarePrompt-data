#State of the program right berfore the function call: arr is a list of integers where 1 <= len(arr) <= 2 * 10^5, and each element a_i in arr satisfies 1 <= a_i <= len(arr).
def func_1(arr):
    i = 0
    j = len(arr) - 1
    while i <= j:
        if arr[i] == arr[j]:
            i += 1
            j -= 1
        else:
            break
        
    #State: The loop will either exit with `i` and `j` such that `i > j` if `arr` is a palindrome, or it will exit with `i <= j` and `arr[i] != arr[j]` if `arr` is not a palindrome.
    if (i > j) :
        return 0
        #The program returns 0.
    #State: The loop will either exit with `i` and `j` such that `i > j` if `arr` is a palindrome, or it will exit with `i <= j` and `arr[i] != arr[j]` if `arr` is not a palindrome. Additionally, `i` is less than or equal to `j`.
    while arr[i] == arr[i + 1]:
        i += 1
        
    #State: The loop will exit with `i` incremented until `arr[i] != arr[i + 1]` or `i` reaches the end of the array. The value of `j` remains unchanged.
    if (j != len(arr) - 1) :
        return j - i + 1
        #The program returns the difference between `j` and `i` plus 1, where `i` is the index at which the loop exits due to `arr[i] != arr[i + 1]` or `i` reaching the end of the array, and `j` is an index that remains unchanged and is not equal to the length of `arr` minus 1.
    #State: The loop will exit with `i` incremented until `arr[i] != arr[i + 1]` or `i` reaches the end of the array. The value of `j` remains unchanged, and `j` is equal to `len(arr) - 1`.
    return j - i
    #The program returns the difference between `j` and `i`, where `j` is equal to `len(arr) - 1` and `i` is the index at which the loop exits, either because `arr[i] != arr[i + 1]` or because `i` reaches the end of the array.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and checks if the list is a palindrome. If the list is a palindrome, it returns 0. If the list is not a palindrome, it returns the length of the longest prefix or suffix that is a palindrome, adjusted based on the conditions under which the loop exits. Specifically, if the loop exits with `j` not equal to the last index of the array, it returns `j - i + 1`. If the loop exits with `j` equal to the last index of the array, it returns `j - i`.


#State of the program right berfore the function call: arr is a list of integers where the length of the list is n (1 ≤ n ≤ 2 * 10^5), and each element in the list is an integer between 1 and n inclusive.
def func_1(arr):
    i = 0
    j = len(arr) - 1
    while i <= j:
        if arr[i] == arr[j]:
            i += 1
            j -= 1
        else:
            break
        
    #State: Output State: `i` is 1 and `j` is the length of `arr` - 2, or `i` is 0 and `j` is the length of `arr` - 1, and the loop has terminated because `i` is no longer less than or equal to `j`.
    #
    #To explain this in natural language: After all iterations of the loop have finished, the values of `i` and `j` will be such that `i` is 1 and `j` is the second last index of `arr`, or `i` is 0 and `j` is the last index of `arr`. The loop terminates when `i` exceeds `j`, meaning all elements in the array have been compared in pairs from the start and end moving towards the center.
    if (i > j) :
        return 0
        #The program returns 0
    #State: `i` is 1 and `j` is the length of `arr` - 2, or `i` is 0 and `j` is the length of `arr` - 1, and the loop has not terminated because `i` is still less than or equal to `j`.
    while arr[i] == arr[i + 1]:
        i += 1
        
    #State: Output State: `i` is the length of `arr` - 1 and `j` is the length of `arr` - 2, and `arr[i]` must be equal to `arr[i + 1]`.
    #
    #This means that after all iterations of the loop, `i` will be one less than the length of `arr`, and `j` will be `i - 1`. Additionally, every element from `arr[i]` to the end of the array must be equal, as the loop continues to increment `i` as long as `arr[i]` equals `arr[i + 1]`.
    if (j != len(arr) - 1) :
        return j - i + 1
        #The program returns the difference between index j and i plus one, which is the distance between two consecutive elements in the list `arr` that are equal.
    #State: `i` is the length of `arr` - 1 and `j` is the length of `arr` - 2, and `arr[i]` must be equal to `arr[i + 1]`. Additionally, `j` is equal to the length of `arr` - 1
    return j - i
    #The program returns 1
#Overall this is what the function does:The function accepts a list of integers `arr` and returns either 0, the difference between the indices of two consecutive equal elements plus one, or 1. It first checks if any two consecutive elements in the list are equal by comparing elements from both ends of the list towards the center. If no such elements are found, it returns 0. If two consecutive equal elements are found, it returns the distance between them. If no such elements are found after the initial check, it returns 1.


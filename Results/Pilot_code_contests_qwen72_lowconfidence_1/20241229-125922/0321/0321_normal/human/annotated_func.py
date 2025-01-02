#State of the program right berfore the function call: arr is a list of integers where each integer represents the size of a kangaroo, and the length of arr is between 1 and 5·10^5, inclusive. Each element in arr is between 1 and 10^5, inclusive.
def func_1(arr):
    if (len(arr) == 1) :
        return 1
        #The program returns 1
    #State of the program after the if block has been executed: arr is a list of integers where each integer represents the size of a kangaroo, and the length of arr is between 2 and 5·10^5, inclusive. Each element in arr is between 1 and 10^5, inclusive.
    arr.sort()
    start = 0
    move = len(arr) // 2
    ans = len(arr)
    while move < len(arr):
        if arr[start] is None:
            move += 1
        elif arr[start] * 2 > arr[move]:
            move += 1
        else:
            arr[move] = None
            ans -= 1
            move += 1
            start += 1
        
    #State of the program after the loop has been executed: `arr` is a sorted list of integers in ascending order, with some elements set to `None` starting from the middle and moving towards the end, `start` is the number of elements that were processed and set to `None`, `move` is `len(arr)`, and `ans` is the original length of `arr` minus the number of elements that were set to `None`.
    return ans
    #The program returns the original length of `arr` minus the number of elements that were set to `None`.
#Overall this is what the function does:The function `func_1` accepts a list `arr` of integers, where each integer represents the size of a kangaroo. The function returns the maximum number of kangaroos that can be paired such that the size of the larger kangaroo in each pair is at most twice the size of the smaller kangaroo. If the list contains only one element, the function returns 1. After the function executes, the input list `arr` is sorted in ascending order, and some elements in the list may be set to `None`. The returned value is the original length of `arr` minus the number of elements that were set to `None`.


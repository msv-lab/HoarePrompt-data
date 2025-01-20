#State of the program right berfore the function call: arr is a list of positive integers.
def func_1(arr):
    n = len(arr)
    if (n == 0) :
        return 0
        #The program returns 0
    #State of the program after the if block has been executed: *`arr` is a list of positive integers, `n` is the number of elements in `arr`, and `n` is greater than 0
    max_products = [0] * n

max_products[0] = arr[0]
    for i in range(1, n):
        max_products[i] = arr[i]
        
        for j in range(i):
            if arr[j] < arr[i]:
                max_products[i] = max(max_products[i], max_products[j] * arr[i])
        
    #State of the program after the  for loop has been executed: After the loop finishes executing, `arr` remains a list of positive integers, `n` is the number of elements in `arr` and is greater than 0, `max_products` is a list of length `n` where each element `max_products[i]` (for `i > 0`) is the maximum product of `arr[i]` with any subsequence of previous elements in `arr` that are less than `arr[i]`. If no such subsequence exists, `max_products[i]` is simply `arr[i]`. The loop does not execute if `n` is less than or equal to 1. After the loop, `i` is `n` and `j` is `n-1`.
    return max(max_products)
    #The program returns the maximum value from the list `max_products`, which contains the maximum products of each element in `arr` with any subsequence of previous elements in `arr` that are less than the current element, or the element itself if no such subsequence exists.
#Overall this is what the function does:-


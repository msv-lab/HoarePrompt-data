#State of the program right berfore the function call: n is an integer such that 2 <= n <= 100, and arr is a list of n integers where 1 <= arr[i] <= 10^9.
def func_1(n, arr):
    arr.sort()
    new_arr = []
    left = 0
    right = n - 1
    while left <= right:
        if left == right:
            new_arr.append(arr[left])
        else:
            new_arr.append(arr[right])
            new_arr.append(arr[left])
        
        left += 1
        
        right -= 1
        
    #State: `left` is `n`, `right` is `-1`, `new_arr` is a list containing all elements of `arr` in a mirrored order, starting from the end and alternating with the start.
    max_beauty = 0
    for i in range(1, n):
        max_beauty += abs(new_arr[i] - new_arr[i - 1])
        
    #State: `left` is `n`, `right` is `-1`, `new_arr` is the same as initially constructed, `max_beauty` is the sum of the absolute differences between consecutive elements of `new_arr`.
    return max_beauty
    #The program returns the sum of the absolute differences between consecutive elements of `new_arr`.
#Overall this is what the function does:The function `func_1` accepts an integer `n` and a list `arr` of `n` integers. It sorts the list `arr` and then constructs a new list `new_arr` by appending elements from `arr` in a mirrored order, starting from the end and alternating with the start. The function then calculates the sum of the absolute differences between consecutive elements of `new_arr` and returns this sum. After the function concludes, `new_arr` contains all elements of `arr` in the described mirrored order, and the program returns the computed sum of absolute differences.


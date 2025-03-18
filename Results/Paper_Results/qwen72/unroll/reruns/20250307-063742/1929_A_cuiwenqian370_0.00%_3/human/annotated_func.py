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
        
    #State: `left` is `n`, `right` is `-1`, `new_arr` is a list containing the elements of `arr` in a mirrored order, starting from the end and then the beginning, with the middle element (if `n` is odd) appearing only once.
    max_beauty = 0
    for i in range(1, n):
        max_beauty += abs(new_arr[i] - new_arr[i - 1])
        
    #State: `left` is `n`, `right` is `-1`, `new_arr` is a list containing the elements of `arr` in a mirrored order, starting from the end and then the beginning, with the middle element (if `n` is odd) appearing only once, `max_beauty` is the sum of the absolute differences between consecutive elements in `new_arr` from index 1 to index `n-1`.
    return max_beauty
    #The program returns the sum of the absolute differences between consecutive elements in `new_arr` from index 1 to index `n-1`. `new_arr` is a list containing the elements of `arr` in a mirrored order, starting from the end and then the beginning, with the middle element (if `n` is odd) appearing only once.
#Overall this is what the function does:The function `func_1` accepts an integer `n` and a list `arr` of `n` integers. It returns the sum of the absolute differences between consecutive elements in a new list `new_arr`, which is constructed by sorting `arr` and then arranging its elements in a mirrored order, starting from the largest element and alternating with the smallest remaining element. If `n` is odd, the middle element appears only once in `new_arr`.


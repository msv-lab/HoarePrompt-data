#State of the program right berfore the function call: n is an integer such that 2 <= n <= 100, and arr is a list of n integers where 1 <= arr[i] <= 10^9 for all 0 <= i < n.
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
        
    #State: `n` is an integer such that 2 <= n <= 100, `arr` is a sorted list of `n` integers where 1 <= `arr[i]` <= 10^9 for all 0 <= i < n, `left` is `n`, `right` is `-1`, `new_arr` contains all elements of `arr` in a mirrored order, starting from the last element and then the first element, followed by the second-to-last element and then the second element, and so on. If `n` is odd, the middle element of `arr` will be the last element in `new_arr`.
    max_beauty = 0
    for i in range(1, n):
        max_beauty += abs(new_arr[i] - new_arr[i - 1])
        
    #State: `n` is an integer such that 2 <= n <= 100, `arr` is a sorted list of `n` integers where 1 <= `arr[i]` <= 10^9 for all 0 <= i < n, `left` is `n`, `right` is `-1`, `new_arr` contains all elements of `arr` in a mirrored order, `max_beauty` is the sum of the absolute differences between consecutive elements in `new_arr`, `i` is `n-1`.
    return max_beauty
    #The program returns the sum of the absolute differences between consecutive elements in the mirrored list `new_arr`.
#Overall this is what the function does:The function `func_1` accepts an integer `n` and a list `arr` of `n` integers. It sorts the list `arr` and then constructs a new list `new_arr` by placing the elements in a mirrored order: starting from the last element and then the first element, followed by the second-to-last element and then the second element, and so on. If `n` is odd, the middle element of `arr` will be the last element in `new_arr`. The function returns the sum of the absolute differences between consecutive elements in `new_arr`.


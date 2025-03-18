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
        
    #State: `new_arr` is a list containing all elements of `arr` in a reversed order, but with elements paired from the ends towards the center. If `n` is odd, the middle element is appended only once at the end. `left` is `n`, and `right` is `-1`.
    max_beauty = 0
    for i in range(1, n):
        max_beauty += abs(new_arr[i] - new_arr[i - 1])
        
    #State: `max_beauty` is the sum of the absolute differences between consecutive elements in `new_arr`. `left` is `n`, `right` is `-1`, `new_arr` is unchanged.
    return max_beauty
    #The program returns the sum of the absolute differences between consecutive elements in `new_arr`.
#Overall this is what the function does:The function `func_1` accepts an integer `n` and a list of `n` integers `arr`. It sorts `arr` and then creates a new list `new_arr` by pairing elements from the ends of the sorted list towards the center. If `n` is odd, the middle element is appended only once at the end. The function returns the sum of the absolute differences between consecutive elements in `new_arr`.


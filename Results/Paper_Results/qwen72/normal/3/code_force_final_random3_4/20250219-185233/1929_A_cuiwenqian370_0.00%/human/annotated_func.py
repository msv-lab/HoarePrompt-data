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
        
    #State: `n` is an integer such that 2 <= n <= 100, `arr` is a sorted list of `n` integers where 1 <= `arr[i]` <= 10^9 for all 0 <= i < n, `left` is `n`, `right` is `-1`, `new_arr` is a list containing all elements of `arr` in a modified order. If `n` is odd, the middle element of `arr` is appended to `new_arr` once. If `n` is even, all elements of `arr` are appended to `new_arr` in pairs, with each pair consisting of the rightmost and leftmost elements of the current subarray of `arr` at each iteration.
    max_beauty = 0
    for i in range(1, n):
        max_beauty += abs(new_arr[i] - new_arr[i - 1])
        
    #State: `n` is an integer such that 2 <= n <= 100, `i` is `n-1`, `left` is `n`, `right` is `-1`, `new_arr` is a list containing all elements of `arr` in a modified order, `max_beauty` is the sum of the absolute differences between consecutive elements in `new_arr`.
    return max_beauty
    #The program returns the sum of the absolute differences between consecutive elements in `new_arr`, where `new_arr` is a list containing all elements of `arr` in a modified order.
#Overall this is what the function does:The function `func_1` accepts an integer `n` and a list `arr` of `n` integers. It returns the sum of the absolute differences between consecutive elements in a modified list `new_arr`, which contains all elements of `arr` but arranged in a specific order: elements are paired from the largest to the smallest, with the largest element followed by the smallest, and so on. If `n` is odd, the middle element of `arr` is appended to `new_arr` once. The final state of the program ensures that `new_arr` is a permutation of `arr` and the returned value is the computed sum of these absolute differences.


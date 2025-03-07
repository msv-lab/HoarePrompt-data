#State of the program right berfore the function call: n is an integer such that 2 <= n <= 100, and arr is a list of integers where each integer a_i satisfies 1 <= a_i <= 10^9, and the length of arr is equal to n.
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
        
    #State: - `new_arr` will contain all elements of `arr` in a new order: the largest element, the smallest element, the second largest element, the second smallest element, and so on.
    #- `left` will be greater than `right`, indicating that the loop has finished executing.
    #- `right` will be one less than `left`.
    #
    #In natural language, after all iterations of the loop, `new_arr` will have the elements of `arr` rearranged such that they alternate between the largest and smallest remaining elements. The variables `left` and `right` will no longer satisfy the condition `left <= right`, meaning `left` will be greater than `right`.
    #
    #Output State:
    max_beauty = 0
    for i in range(1, n):
        max_beauty += abs(new_arr[i] - new_arr[i - 1])
        
    #State: `new_arr` will contain all elements of `arr` in a new order: the largest element, the smallest element, the second largest element, the second smallest element, and so on; `left` will be greater than `right`, indicating that the loop has finished executing; `right` will be one less than `left`; `max_beauty` is the sum of the absolute differences between all consecutive elements in `new_arr` from `new_arr[0]` to `new_arr[n-1]`.
    return max_beauty
    #The program returns `max_beauty`, which is the sum of the absolute differences between all consecutive elements in `new_arr` from `new_arr[0]` to `new_arr[n-1]`.
#Overall this is what the function does:The function takes an integer `n` and a list of integers `arr` of length `n`, sorts the list, and then rearranges it such that the elements alternate between the largest and smallest remaining elements. It calculates and returns `max_beauty`, which is the sum of the absolute differences between all consecutive elements in this rearranged list.


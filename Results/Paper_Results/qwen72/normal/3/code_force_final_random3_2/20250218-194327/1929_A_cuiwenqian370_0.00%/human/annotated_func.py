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
        
    #State: `n` is an integer such that 2 <= n <= 100, `arr` is a sorted list of `n` integers where 1 <= `arr[i]` <= 10^9 for all 0 <= i < n, `left` is `n`, `right` is `-1`, `new_arr` contains all elements of `arr` in a pattern where the last element is appended first, followed by the first element, then the second-to-last element, followed by the second element, and so on. If `n` is odd, the middle element is appended last.
    max_beauty = 0
    for i in range(1, n):
        max_beauty += abs(new_arr[i] - new_arr[i - 1])
        
    #State: `n` is an integer such that 2 <= n <= 100, `i` is `n-1`, `arr` is a sorted list of `n` integers where 1 <= `arr[i]` <= 10^9 for all 0 <= i < n, `left` is `n`, `right` is `-1`, `new_arr` contains all elements of `arr` in the specified pattern, `max_beauty` is the sum of the absolute differences between consecutive elements in `new_arr` from index 1 to `n-1`.
    return max_beauty
    #The program returns the sum of the absolute differences between consecutive elements in `new_arr` from index 1 to `n-1`, where `new_arr` contains all elements of `arr` in a specified pattern. `arr` is a sorted list of `n` integers, and `n` is an integer such that 2 <= n <= 100.
#Overall this is what the function does:The function `func_1` accepts an integer `n` and a list of integers `arr`, where `2 <= n <= 100` and each element in `arr` is an integer such that `1 <= arr[i] <= 10^9`. It returns the sum of the absolute differences between consecutive elements in a new list `new_arr`, which is constructed by rearranging the elements of the sorted `arr` in a specific pattern: the last element is appended first, followed by the first element, then the second-to-last element, followed by the second element, and so on. If `n` is odd, the middle element is appended last. The final state of the program includes `arr` being sorted, `new_arr` containing the rearranged elements, and `max_beauty` holding the computed sum of absolute differences.


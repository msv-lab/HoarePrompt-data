#State of the program right berfore the function call: n is an integer such that 2 <= n <= 100, and arr is a list of integers of length n where each integer a_i satisfies 1 <= a_i <= 10^9.
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
        
    #State: `new_arr` is a rearranged list of `arr` with elements ordered as largest, smallest, second largest, second smallest, etc.; `left` is `n // 2 + 1` if `n` is odd, or `n // 2` if `n` is even; `right` is `n // 2 - 1`.
    max_beauty = 0
    for i in range(1, n):
        max_beauty += abs(new_arr[i] - new_arr[i - 1])
        
    #State: `new_arr` is a rearranged list of `arr` with elements ordered as largest, smallest, second largest, second smallest, etc.; `left` is `n // 2 + 1` if `n` is odd, or `n // 2` if `n` is even; `right` is `n // 2 - 1`; `max_beauty` is `max_beauty_final`.
    return max_beauty
    #The program returns max_beauty which is equal to max_beauty_final.
#Overall this is what the function does:The function `func_1` takes an integer `n` and a list of integers `arr` of length `n`. It rearranges the list such that the elements are ordered as largest, smallest, second largest, second smallest, and so on. The function then calculates and returns the sum of the absolute differences between consecutive elements in this rearranged list, which is referred to as `max_beauty`.


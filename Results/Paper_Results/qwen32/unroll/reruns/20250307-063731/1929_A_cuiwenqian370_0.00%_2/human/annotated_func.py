#State of the program right berfore the function call: n is an integer such that 2 <= n <= 100, and arr is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^9.
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
        
    #State: `new_arr` is a rearranged list of `arr` with elements paired from largest to smallest, `left` is `n`, `right` is `n - 1`, `arr` remains unchanged, `n` remains unchanged.
    max_beauty = 0
    for i in range(1, n):
        max_beauty += abs(new_arr[i] - new_arr[i - 1])
        
    #State: `new_arr` is a rearranged list of `arr` with elements paired from largest to smallest, `left` is `n`, `right` is `n - 1`, `arr` remains unchanged, `n` remains unchanged, `max_beauty` is the sum of absolute differences between consecutive elements of `new_arr`.
    return max_beauty
    #The program returns `max_beauty`, which is the sum of absolute differences between consecutive elements of `new_arr`.
#Overall this is what the function does:The function takes an integer `n` and a list `arr` of `n` integers, rearranges the list by pairing the largest and smallest elements consecutively, and returns the sum of the absolute differences between consecutive elements of this rearranged list.


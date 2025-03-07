#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 100, and arr is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9.
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
        
    #State: - `left` will be equal to `right + 1` after the loop terminates.
    #- `right` will be equal to `left - 1`.
    #- `new_arr` will contain all elements of `arr` but arranged such that the largest elements come first, followed by the smallest elements, alternating between the two extremes.
    #
    #Given the initial conditions and the behavior of the loop, the final state can be described as:
    #- `left` will be `n // 2 + 1` if `n` is odd, or `n // 2` if `n` is even.
    #- `right` will be `n // 2 - 1` if `n` is odd, or `n // 2 - 1` if `n` is even.
    #- `new_arr` will be a list where the elements are arranged in the described alternating order.
    #
    #Thus, the final output state is:
    #
    #Output State:
    max_beauty = 0
    for i in range(1, n):
        max_beauty += abs(new_arr[i] - new_arr[i - 1])
        
    #State: `left` will be equal to `right + 1` after the loop terminates; `right` will be equal to `left - 1`; `new_arr` will contain all elements of `arr` but arranged such that the largest elements come first, followed by the smallest elements, alternating between the two extremes; `max_beauty` is the sum of the absolute differences between all consecutive elements in `new_arr` from index 1 to `n-1`.
    return max_beauty
    #The program returns `max_beauty`, which is the sum of the absolute differences between all consecutive elements in `new_arr` from index 1 to `n-1`.
#Overall this is what the function does:The function takes an integer `n` and a list `arr` of `n` integers, sorts the list, and rearranges it such that the largest and smallest elements alternate. It then calculates and returns the sum of the absolute differences between consecutive elements in this rearranged list.


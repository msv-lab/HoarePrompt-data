#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 100, and arr is a list of n integers where each integer is in the range 1 ≤ arr[i] ≤ 10^9.
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
        
    #State: Output State: `left` is `n - 1`, `right` is 1, and `new_arr` is a list containing all elements from `arr` but in reverse order.
    #
    #Explanation: After the loop completes all its iterations, `left` will be equal to `right + 1`, which means `left` will be `n - 1` and `right` will be 1. During each iteration, the loop appends elements from the ends towards the center of the original array `arr` into `new_arr`. Therefore, `new_arr` will contain all elements of `arr` in reverse order.
    max_beauty = 0
    for i in range(1, n):
        max_beauty += abs(new_arr[i] - new_arr[i - 1])
        
    #State: Output State: `max_beauty` is increased by the sum of absolute differences between consecutive elements from index 1 to `left + 1` in the `new_arr` list, `i` is equal to `n`, `n` is equal to `left + 1`, and the values of `left`, `right`, and `new_arr` remain unchanged.
    #
    #To break it down further:
    #- The loop iterates from `i = 1` to `i = n-1` (where `n` is initially `left + 1`), adding the absolute difference between `new_arr[i]` and `new_arr[i - 1]` to `max_beauty`.
    #- After all iterations, `max_beauty` will contain the total sum of these absolute differences.
    #- The values of `left`, `right`, and `new_arr` remain unchanged because they are not modified within the loop.
    #- `i` will be equal to `n` after the last iteration, which is `left + 1`.
    #- `n` will also be equal to `left + 1` after the loop completes.
    return max_beauty
    #The program returns max_beauty which is increased by the sum of absolute differences between consecutive elements from index 1 to left + 1 in the new_arr list, where i is equal to n (which is left + 1), and the values of left, right, and new_arr remain unchanged.
#Overall this is what the function does:The function accepts an integer `n` (where 2 ≤ n ≤ 100) and a list `arr` of `n` integers (each integer in the range 1 ≤ arr[i] ≤ 10^9). It sorts the list `arr` and then creates a new list `new_arr` by appending elements from the ends of `arr` towards the center, resulting in `new_arr` containing all elements of `arr` in reverse order. Finally, it calculates `max_beauty` as the sum of the absolute differences between consecutive elements from index 1 to `left + 1` in `new_arr`, where `left` is `n - 1`, and returns `max_beauty`. The values of `left`, `right`, and `new_arr` remain unchanged after the function execution.


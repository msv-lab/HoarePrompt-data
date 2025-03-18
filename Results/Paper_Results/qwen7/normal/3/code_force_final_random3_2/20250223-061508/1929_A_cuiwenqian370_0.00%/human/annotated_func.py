#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 100, and arr is a list of n integers where each integer satisfies 1 ≤ arr[i] ≤ 10^9 for all 0 ≤ i < n.
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
        
    #State: Output State: `left` is `n - 1`, `right` is 0, and `new_arr` is a list containing all elements from `arr[0]` to `arr[n-1]` in a specific order.
    #
    #Explanation: After the loop completes all its iterations, `left` will be equal to `right + 1`, meaning `left` will be `n - 1` and `right` will be 0. The `new_arr` list will contain all elements from the original array `arr`, but in a specific order where elements from the end of the array are added before elements from the beginning, except when `left` equals `right`, in which case only one element is appended.
    max_beauty = 0
    for i in range(1, n):
        max_beauty += abs(new_arr[i] - new_arr[i - 1])
        
    #State: Output State: `max_beauty` is the sum of the absolute differences between each consecutive pair of elements in `new_arr` from index 1 to `n-1`.
    #
    #In natural language, after the loop executes all its iterations, `max_beauty` will hold the total beauty calculated as the sum of the absolute differences between every adjacent pair of elements in the `new_arr` list, starting from `new_arr[1]` up to `new_arr[n-1]`. The value of `i` will be `n`, and the loop will have iterated `n-1` times, covering all possible pairs of consecutive elements in `new_arr`.
    return max_beauty
    #`The program returns max_beauty which is the sum of the absolute differences between each consecutive pair of elements in new_arr from index 1 to n-1`
#Overall this is what the function does:The function accepts an integer `n` and a list `arr` of `n` integers. It first sorts the list `arr`. Then, it constructs a new list `new_arr` by alternating elements from the end and beginning of the sorted list, except when only one element remains, in which case it adds that element. Finally, it calculates and returns `max_beauty`, which is the sum of the absolute differences between each consecutive pair of elements in `new_arr` from index 1 to `n-1`.


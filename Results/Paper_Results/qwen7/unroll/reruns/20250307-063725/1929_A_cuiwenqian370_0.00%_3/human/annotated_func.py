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
        
    #State: The `new_arr` will contain elements from `arr` such that for every pair of elements, the rightmost element is followed by the leftmost element of the current subarray being considered, until the middle of the array is reached.
    max_beauty = 0
    for i in range(1, n):
        max_beauty += abs(new_arr[i] - new_arr[i - 1])
        
    #State: Output State: `max_beauty` is the sum of absolute differences between consecutive elements in `new_arr` from index 1 to n-1.
    return max_beauty
    #The program returns max_beauty which is the sum of absolute differences between consecutive elements in new_arr from index 1 to n-1.
#Overall this is what the function does:The function accepts an integer `n` (where 2 ≤ n ≤ 100) and a list `arr` of `n` integers (each in the range 1 ≤ arr[i] ≤ 10^9). It sorts the list `arr` and then constructs a new list `new_arr` by alternating between the largest and smallest remaining elements from the sorted list. After constructing `new_arr`, it calculates the sum of the absolute differences between each pair of consecutive elements in `new_arr` from index 1 to n-1 and returns this sum as `max_beauty`.


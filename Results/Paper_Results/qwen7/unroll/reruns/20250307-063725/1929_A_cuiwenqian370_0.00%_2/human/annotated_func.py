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
        
    #State: new_arr is a list containing all elements from arr, but in reverse order.
    max_beauty = 0
    for i in range(1, n):
        max_beauty += abs(new_arr[i] - new_arr[i - 1])
        
    #State: Output State: `new_arr` is a list containing all elements from `arr` in reverse order; `max_beauty` is the sum of absolute differences between each pair of consecutive elements in `new_arr` starting from index 1 to n-1.
    return max_beauty
    #The program returns the maximum beauty which is the sum of absolute differences between each pair of consecutive elements in the reversed list `new_arr` starting from index 1 to n-1.
#Overall this is what the function does:The function accepts an integer `n` (where 2 ≤ n ≤ 100) and a list `arr` of `n` integers (each in the range 1 ≤ arr[i] ≤ 10^9). It first sorts the list `arr`, then creates a new list `new_arr` by appending elements from `arr` in reverse order. After that, it calculates the maximum beauty, defined as the sum of absolute differences between each pair of consecutive elements in `new_arr` starting from index 1 to n-1. Finally, it returns this maximum beauty.


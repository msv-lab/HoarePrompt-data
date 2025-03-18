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
        
    #State: new_arr is a list of `n` integers where elements are arranged in the order of largest, smallest, second largest, second smallest, and so on, starting with the largest element; `left` is `n`; `right` is `n - 1`.
    max_beauty = 0
    for i in range(1, n):
        max_beauty += abs(new_arr[i] - new_arr[i - 1])
        
    #State: `new_arr` is a list of `n` integers where elements are arranged in the order of largest, smallest, second largest, second smallest, and so on, starting with the largest element; `left` is `n`; `right` is `n - 1`; `max_beauty` is the sum of the absolute differences between consecutive elements in `new_arr`.
    return max_beauty
    #The program returns `max_beauty`, which is the sum of the absolute differences between consecutive elements in `new_arr`.
#Overall this is what the function does:The function accepts an integer `n` and a list `arr` of `n` integers, where each integer in `arr` is between 1 and \(10^9\) inclusive. It returns `max_beauty`, which is the sum of the absolute differences between consecutive elements in a new list `new_arr` that is constructed by arranging the elements of `arr` in a specific order: starting with the largest element, then the smallest, followed by the second largest, second smallest, and so on.


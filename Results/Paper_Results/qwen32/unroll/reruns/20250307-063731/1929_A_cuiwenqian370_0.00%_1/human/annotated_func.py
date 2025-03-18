#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, for each test case n is an integer such that 2 <= n <= 100, and arr is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^9.
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
        
    #State: `new_arr` is a list that contains the elements of `arr` rearranged such that the largest remaining element is placed before the smallest remaining element, continuing this pattern until all elements are used; `left` is `n // 2 + 1` if `n` is odd, or `n // 2` if `n` is even; `right` is `n // 2 - 1` if `n` is odd, or `n // 2 - 1` if `n` is even (essentially, `left` and `right` have crossed each other).
    max_beauty = 0
    for i in range(1, n):
        max_beauty += abs(new_arr[i] - new_arr[i - 1])
        
    #State: new_arr is a list that contains the elements of arr rearranged such that the largest remaining element is placed before the smallest remaining element, continuing this pattern until all elements are used; left is n // 2 + 1 if n is odd, or n // 2 if n is even; right is n // 2 - 1 if n is odd, or n // 2 - 1 if n is even; max_beauty is the sum of the absolute differences between consecutive elements in new_arr.
    return max_beauty
    #The program returns max_beauty, which is the sum of the absolute differences between consecutive elements in new_arr.
#Overall this is what the function does:The function `func_1` takes an integer `n` and a list `arr` of `n` integers, sorts the list, and rearranges it such that the largest and smallest elements alternate. It then calculates and returns `max_beauty`, which is the sum of the absolute differences between consecutive elements in this rearranged list.


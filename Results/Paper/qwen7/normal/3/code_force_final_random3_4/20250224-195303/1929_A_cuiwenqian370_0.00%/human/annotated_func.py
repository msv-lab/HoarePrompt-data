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
        
    #State: Output State: `left` is `n`, `right` is `-1`, and `new_arr` is a list containing all elements from `arr` but in a specific order. Specifically, the elements are appended to `new_arr` in pairs starting from the ends towards the center. If there is an odd number of elements in `arr`, the middle element will be the last element in `new_arr`.
    #
    #To elaborate, the loop continues until `left` exceeds `right`. During each iteration, if `left` equals `right`, the single element at `left` (or `right`) is appended to `new_arr`. Otherwise, the elements at `right` and `left` are appended to `new_arr` in that order. After each iteration, `left` is incremented and `right` is decremented. Once the loop finishes, `left` will be equal to `n` (since it starts at 0 and is incremented until it reaches `n`), `right` will be `-1` (since it starts at `n-1` and is decremented until it goes below 0), and `new_arr` will contain all elements from `arr` in the described order.
    max_beauty = 0
    for i in range(1, n):
        max_beauty += abs(new_arr[i] - new_arr[i - 1])
        
    #State: Output State: The value of `max_beauty` is the sum of the absolute differences between every consecutive pair of elements in `new_arr` from index 1 to `n-1`.
    #
    #This means that after the loop has executed all its iterations (from `i = 1` to `i = n-1`), `max_beauty` will hold the total sum of the absolute differences between each adjacent pair of elements in the `new_arr` list.
    return max_beauty
    #The program returns the maximum beauty which is the sum of the absolute differences between every consecutive pair of elements in the `new_arr` list from index 1 to `n-1`.
#Overall this is what the function does:The function accepts an integer `n` (where 2 ≤ n ≤ 100) and a list `arr` of `n` integers (each between 1 and 10^9). It first sorts the list `arr`. Then, it creates a new list `new_arr` by appending elements from the end and start of the sorted `arr` alternately until all elements are used. If the length of `arr` is odd, the middle element is placed at the end. Finally, it calculates the maximum beauty as the sum of the absolute differences between every consecutive pair of elements in `new_arr` from index 1 to `n-1`, and returns this value.


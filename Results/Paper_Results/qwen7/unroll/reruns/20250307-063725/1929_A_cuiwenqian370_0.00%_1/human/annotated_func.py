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
        
    #State: new_arr is a list containing every second element from the original arr, starting from the first and last elements respectively, until the middle of the list.
    max_beauty = 0
    for i in range(1, n):
        max_beauty += abs(new_arr[i] - new_arr[i - 1])
        
    #State: Output State: new_arr is a list containing every second element from the original arr, starting from the first and last elements respectively, until the middle of the list; max_beauty is the sum of absolute differences between consecutive elements in new_arr.
    return max_beauty
    #The program returns the sum of absolute differences between consecutive elements in the list new_arr, which contains every second element from the original arr, starting from the first and last elements respectively, until the middle of the list.
#Overall this is what the function does:The function accepts two parameters: `n`, an integer between 2 and 100, and `arr`, a list of `n` integers where each integer is between 1 and 10^9. It sorts the list `arr`. Then, it creates a new list `new_arr` containing every second element from the original `arr`, starting from the first and last elements respectively, until the middle of the list. Finally, it calculates and returns the sum of absolute differences between consecutive elements in `new_arr`.


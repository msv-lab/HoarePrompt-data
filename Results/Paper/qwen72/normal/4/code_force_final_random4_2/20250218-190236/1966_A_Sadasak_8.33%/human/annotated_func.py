#State of the program right berfore the function call: arr is a list of integers where 1 <= len(arr) <= 100 and 1 <= arr[i] <= 100 for all i, and k is an integer such that 2 <= k <= 100.
def func_1(arr, k):
    frequency_table = {}
    for num in arr:
        frequency_table[num] = frequency_table.get(num, 0) + 1
        
        if frequency_table[num] > k:
            frequency_table[num] = k
        
    #State: `arr` is a list of integers where 1 <= len(arr) <= 100 and 1 <= arr[i] <= 100 for all i, `k` is an integer such that 2 <= k <= 100, `frequency_table` is a dictionary where each key is an integer from the list `arr`, and the value for each key is the minimum of the count of that integer in `arr` and `k`.
    return frequency_table
    #The program returns a dictionary `frequency_table` where each key is an integer from the list `arr`, and the value for each key is the minimum of the count of that integer in `arr` and `k`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and an integer `k`. It returns a dictionary `frequency_table` where each key is an integer from `arr`, and the value for each key is the count of that integer in `arr`, capped at `k` if the count exceeds `k`. The function does not modify the input list `arr` or the integer `k`.


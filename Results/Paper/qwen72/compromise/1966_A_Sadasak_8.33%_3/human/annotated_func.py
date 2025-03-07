#State of the program right berfore the function call: arr is a list of integers where 1 <= len(arr) <= 100 and 1 <= arr[i] <= 100 for all i, and k is an integer such that 2 <= k <= 100.
def func_1(arr, k):
    frequency_table = {}
    for num in arr:
        frequency_table[num] = frequency_table.get(num, 0) + 1
        
        if frequency_table[num] > k:
            frequency_table[num] = k
        
    #State: `frequency_table` is a dictionary where each key is an integer from the list `arr`, and the value associated with each key is the frequency of that integer in `arr`, but capped at `k`. The list `arr` and the integer `k` remain unchanged.
    return frequency_table
    #The program returns the dictionary `frequency_table` where each key is an integer from the list `arr`, and the value associated with each key is the frequency of that integer in `arr`, but capped at `k`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and an integer `k`, and returns a dictionary `frequency_table`. Each key in `frequency_table` is an integer from `arr`, and the value associated with each key is the frequency of that integer in `arr`, but capped at `k`. The original list `arr` and the integer `k` remain unchanged.


#State of the program right berfore the function call: arr is a list of integers where 1 <= len(arr) <= 100, and each integer in arr is within the range 1 <= arr[i] <= 100. k is an integer such that 2 <= k <= 100.
def func_1(arr, k):
    frequency_table = {}
    for num in arr:
        frequency_table[num] = frequency_table.get(num, 0) + 1
        
        if frequency_table[num] > k:
            frequency_table[num] = k
        
    #State: `frequency_table` is a dictionary where each key is an integer from the list `arr`, and each value is the frequency of the corresponding integer in `arr`, capped at `k`.
    return frequency_table
    #The program returns the dictionary `frequency_table` where each key is an integer from the list `arr`, and each value is the frequency of the corresponding integer in `arr`, capped at `k`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and an integer `k`. It returns a dictionary `frequency_table` where each key is an integer from `arr`, and each value represents the frequency of the corresponding integer in `arr`, with a maximum value of `k`. If an integer appears more than `k` times in `arr`, its frequency in the dictionary is capped at `k`.


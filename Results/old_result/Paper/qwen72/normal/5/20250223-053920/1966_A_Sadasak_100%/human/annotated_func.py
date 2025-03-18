#State of the program right berfore the function call: arr is a list of integers where 1 <= len(arr) <= 100, and k is an integer such that 2 <= k <= 100. Each integer in arr satisfies 1 <= arr[i] <= 100.
def func_1(arr, k):
    frequency_table = {}
    for num in arr:
        frequency_table[num] = frequency_table.get(num, 0) + 1
        
        if frequency_table[num] > k:
            frequency_table[num] = k
        
    #State: `frequency_table` is a dictionary where each key is an integer from `arr`, and the value for each key is the frequency of that integer in `arr`, capped at `k`. The values of `arr` and `k` remain unchanged.
    return frequency_table
    #The program returns the `frequency_table` dictionary where each key is an integer from `arr`, and the value for each key is the frequency of that integer in `arr`, capped at `k`. The values of `arr` and `k` remain unchanged.
#Overall this is what the function does:The function `func_1` accepts a list `arr` of integers and an integer `k`. It returns a dictionary `frequency_table` where each key is an integer from `arr`, and the value for each key is the frequency of that integer in `arr`, capped at `k`. The values of `arr` and `k` remain unchanged.


#State of the program right berfore the function call: arr is a list of integers representing the numbers on the cards, and k is an integer such that 2 <= k <= 100.
def func_1(arr, k):
    frequency_table = {}
    for num in arr:
        frequency_table[num] = frequency_table.get(num, 0) + 1
        
        if frequency_table[num] > k:
            frequency_table[num] = k
        
    #State: Output State: The `frequency_table` dictionary contains each number from the list `arr` as a key, and its value is capped at `k`. If a number appears more than `k` times in `arr`, its value in `frequency_table` will be `k`; otherwise, it will be the actual count of the number in `arr`.
    return frequency_table
    #The program returns a dictionary named `frequency_table` where each key is a number from the list `arr`, and its value is capped at `k`. If a number appears more than `k` times in `arr`, its value in `frequency_table` will be `k`; otherwise, it will be the actual count of the number in `arr`.
#Overall this is what the function does:The function accepts a list of integers `arr` and an integer `k` (where 2 ≤ k ≤ 100). It returns a dictionary `frequency_table` where each key is a number from `arr`, and its value is capped at `k`. If any number in `arr` appears more than `k` times, its value in `frequency_table` will be set to `k`; otherwise, it will be the actual count of that number in `arr`.


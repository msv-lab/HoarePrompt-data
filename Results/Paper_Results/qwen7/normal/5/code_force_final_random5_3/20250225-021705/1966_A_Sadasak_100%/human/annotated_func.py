#State of the program right berfore the function call: arr is a list of integers representing the numbers on the cards, and k is an integer such that 2 <= k <= 100.
def func_1(arr, k):
    frequency_table = {}
    for num in arr:
        frequency_table[num] = frequency_table.get(num, 0) + 1
        
        if frequency_table[num] > k:
            frequency_table[num] = k
        
    #State: Output State: After the loop executes all iterations, `arr` is a list of integers, and for every unique number `num` in `arr`, `frequency_table[num]` will be the minimum value between the count of `num` in `arr` and `k`. If a number appears more than `k` times in `arr`, its count in `frequency_table` will be capped at `k`. All other keys in `frequency_table` will not exist if they were not present in `arr`.
    #
    #This means that for each number in the original list `arr`, the final value in the `frequency_table` will reflect the maximum occurrence of that number up to `k` times, ensuring no number's count exceeds `k` in the `frequency_table`.
    return frequency_table
    #A dictionary named `frequency_table` where each key is a unique number from the list `arr` and the value for each key is the minimum value between the count of that number in `arr` and `k`. If any number appears more than `k` times in `arr`, its count in `frequency_table` will be capped at `k`. All other keys in `frequency_table` will not exist if they were not present in `arr`.
#Overall this is what the function does:The function accepts a list of integers `arr` and an integer `k`. It returns a dictionary `frequency_table` where each key is a unique number from `arr` and the value for each key is the minimum value between the count of that number in `arr` and `k`. If any number appears more than `k` times in `arr`, its count in `frequency_table` will be capped at `k`. All other keys in `frequency_table` will not exist if they were not present in `arr`.


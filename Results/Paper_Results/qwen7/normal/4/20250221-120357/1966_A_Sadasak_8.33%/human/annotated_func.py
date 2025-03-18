#State of the program right berfore the function call: arr is a list of integers representing the numbers on the cards, and k is an integer such that 2 <= k <= 100.
def func_1(arr, k):
    frequency_table = {}
    for num in arr:
        frequency_table[num] = frequency_table.get(num, 0) + 1
        
        if frequency_table[num] > k:
            frequency_table[num] = k
        
    #State: Output State: After the loop executes all the iterations, the `frequency_table` will contain the count of each number in `arr` clamped to a maximum value of `k`. Specifically, for every number `num` in `arr`, `frequency_table[num]` will be the minimum of the actual count of `num` in `arr` and `k`.
    #
    #This means that if a number appears more than `k` times in `arr`, its count in `frequency_table` will be exactly `k`. Otherwise, `frequency_table[num]` will be the exact count of `num` in `arr`.
    return frequency_table
    #The program returns a dictionary `frequency_table` where each key is a number from the list `arr` and its corresponding value is the minimum of the count of that number in `arr` and `k`. If a number appears more than `k` times in `arr`, its count in `frequency_table` will be exactly `k`. Otherwise, the count will be the exact number of times it appears in `arr`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and an integer `k` (where 2 ≤ k ≤ 100). It returns a dictionary `frequency_table` where each key is a number from the list `arr` and its corresponding value is the minimum of the count of that number in `arr` and `k`. If a number appears more than `k` times in `arr`, its count in `frequency_table` will be exactly `k`. Otherwise, the count will be the exact number of times it appears in `arr`.


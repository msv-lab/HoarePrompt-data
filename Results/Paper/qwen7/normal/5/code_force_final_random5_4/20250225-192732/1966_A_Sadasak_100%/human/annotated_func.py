#State of the program right berfore the function call: arr is a list of integers representing the numbers on the cards, and k is an integer such that 2 <= k <= 100.
def func_1(arr, k):
    frequency_table = {}
    for num in arr:
        frequency_table[num] = frequency_table.get(num, 0) + 1
        
        if frequency_table[num] > k:
            frequency_table[num] = k
        
    #State: Output State: After the loop executes all the iterations, `arr` is a non-empty list of integers, and for every integer `num` in `arr`, `frequency_table[num]` is the minimum value between the frequency of `num` in the list `arr` and the integer `k`.
    #
    #In simpler terms, after running through all the elements in the list `arr`, the `frequency_table` will contain each unique number from `arr` with its count capped at `k`. If any number appears more than `k` times in `arr`, its count in `frequency_table` will be set to `k`.
    return frequency_table
    #The program returns a dictionary `frequency_table` where each key is a unique integer from the list `arr` and its corresponding value is the minimum of the frequency of that integer in `arr` and the integer `k`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and an integer `k` (where 2 ≤ k ≤ 100). It processes `arr` to create a dictionary `frequency_table` where each key is a unique integer from `arr` and its value is the minimum frequency of that integer in `arr` capped at `k`. After processing, the function returns this dictionary.


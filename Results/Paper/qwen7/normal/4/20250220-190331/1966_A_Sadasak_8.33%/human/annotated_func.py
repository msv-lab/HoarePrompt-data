#State of the program right berfore the function call: arr is a list of integers representing the numbers on the cards, and k is an integer such that 2 <= k <= 100.
def func_1(arr, k):
    frequency_table = {}
    for num in arr:
        frequency_table[num] = frequency_table.get(num, 0) + 1
        
        if frequency_table[num] > k:
            frequency_table[num] = k
        
    #State: Output State: After the loop executes all its iterations, `arr` will be an empty list, and `frequency_table` will contain the count of each unique number in `arr` capped at `k`.
    #
    #Explanation: The loop iterates over each number in `arr`, incrementing its count in `frequency_table`. If the count of any number exceeds `k`, it is reset to `k`. Once all elements in `arr` have been processed, `arr` becomes empty since all elements have been consumed during iteration. The `frequency_table` will then hold the final counts of each unique number from `arr`, ensuring no count exceeds `k`.
    return frequency_table
    #`frequency_table` is a dictionary containing the count of each unique number from the original `arr`, with all counts capped at `k` and `arr` is an empty list
#Overall this is what the function does:The function accepts a list of integers `arr` and an integer `k` (where 2 ≤ k ≤ 100). It processes `arr` by counting the occurrences of each unique number, ensuring no count exceeds `k`. After processing, it returns a dictionary containing these counts and makes `arr` an empty list.


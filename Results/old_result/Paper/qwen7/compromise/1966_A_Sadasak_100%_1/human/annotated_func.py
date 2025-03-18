#State of the program right berfore the function call: arr is a list of integers representing the numbers on the cards, and k is an integer such that 2 <= k <= 100.
def func_1(arr, k):
    frequency_table = {}
    for num in arr:
        frequency_table[num] = frequency_table.get(num, 0) + 1
        
        if frequency_table[num] > k:
            frequency_table[num] = k
        
    #State: Output State: The `frequency_table` is a dictionary where each key is a number from the list `arr` and its value is the maximum of the occurrences of that number up to `k`. If any number's occurrence exceeds `k`, it is capped at `k`.
    return frequency_table
    #The program returns a dictionary where each key is a number from the list `arr` and its value is the maximum of the occurrences of that number up to `k`. If any number's occurrence exceeds `k`, it is capped at `k`.
#Overall this is what the function does:The function accepts a list of integers `arr` and an integer `k` (where 2 ≤ k ≤ 100). It returns a dictionary where each key is a unique number from the list `arr`, and the corresponding value is the maximum count of that number in the list, capped at `k`. If any number appears more than `k` times in the list, its count is set to `k`.


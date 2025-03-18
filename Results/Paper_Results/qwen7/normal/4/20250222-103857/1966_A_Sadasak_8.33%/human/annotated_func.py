#State of the program right berfore the function call: arr is a list of integers representing the numbers on the cards, and k is an integer such that 2 <= k <= 100.
def func_1(arr, k):
    frequency_table = {}
    for num in arr:
        frequency_table[num] = frequency_table.get(num, 0) + 1
        
        if frequency_table[num] > k:
            frequency_table[num] = k
        
    #State: All values in `frequency_table` are capped at `k`.
    return frequency_table
    #The program returns the frequency_table where all values are capped at k.
#Overall this is what the function does:The function accepts a list of integers `arr` and an integer `k`. It returns a frequency table where each count in the table is capped at `k`. All values in the frequency table are adjusted so that no count exceeds `k`.


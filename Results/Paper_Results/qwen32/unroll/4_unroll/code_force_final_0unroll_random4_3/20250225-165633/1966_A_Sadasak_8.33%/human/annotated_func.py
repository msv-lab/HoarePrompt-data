#State of the program right berfore the function call: arr is a list of integers representing the numbers on the cards, and k is an integer representing the number of cards to exchange in each operation such that 1 <= len(arr) <= 100 and 2 <= k <= 100.
def func_1(arr, k):
    frequency_table = {}
    for num in arr:
        frequency_table[num] = frequency_table.get(num, 0) + 1
        
        if frequency_table[num] > k:
            frequency_table[num] = k
        
    #State: `arr` is a list of integers representing the numbers on the cards, and `k` is an integer representing the number of cards to exchange in each operation such that 1 <= len(arr) <= 100 and 2 <= k <= 100; `frequency_table` is a dictionary where each key is a unique number from `arr` and each value is the minimum of the count of that number in `arr` and `k`.
    return frequency_table
    #The program returns a dictionary `frequency_table` where each key is a unique number from the list `arr` and each value is the minimum of the count of that number in `arr` and `k`.
#Overall this is what the function does:The function takes a list of integers `arr` and an integer `k`, and returns a dictionary where each key is a unique number from `arr` and each value is the minimum of the count of that number in `arr` and `k`.


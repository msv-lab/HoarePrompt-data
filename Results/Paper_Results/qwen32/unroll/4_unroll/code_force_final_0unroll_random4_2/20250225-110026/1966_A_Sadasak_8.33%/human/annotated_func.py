#State of the program right berfore the function call: arr is a list of integers representing the numbers on the cards, and k is an integer representing the number of cards to exchange during each operation such that 2 <= k <= 100 and the length of arr (n) satisfies 1 <= n <= 100.
def func_1(arr, k):
    frequency_table = {}
    for num in arr:
        frequency_table[num] = frequency_table.get(num, 0) + 1
        
        if frequency_table[num] > k:
            frequency_table[num] = k
        
    #State: `arr` is a list of integers representing the numbers on the cards, `k` is an integer representing the number of cards to exchange during each operation such that 2 <= k <= 100 and the length of `arr` (n) satisfies 1 <= n <= 100; `frequency_table` is a dictionary where each key is a unique number from `arr` and each value is the minimum of the count of that number in `arr` and `k`.
    return frequency_table
    #The program returns `frequency_table`, which is a dictionary where each key is a unique number from the list `arr` and each value is the minimum of the count of that number in `arr` and `k`.
#Overall this is what the function does:The function takes a list of integers `arr` and an integer `k`, and returns a dictionary where each key is a unique number from `arr` and each value is the minimum of the count of that number in `arr` and `k`.


#State of the program right berfore the function call: arr is a list of integers where each integer represents the number written on a card, and k is an integer such that 2 <= k <= 100. The length of arr (number of cards) is n, where 1 <= n <= 100. The input consists of multiple test cases, each with a different n and k, and a corresponding list of integers arr.
def func_1(arr, k):
    frequency_table = {}
    for num in arr:
        frequency_table[num] = frequency_table.get(num, 0) + 1
        
        if frequency_table[num] > k:
            frequency_table[num] = k
        
    #State: `frequency_table` contains each unique number from `arr` as keys, with values representing the minimum of the number's occurrences in `arr` and `k`.
    return frequency_table
    #The program returns a dictionary `frequency_table` where each key is a unique number from the list `arr`, and each value is the minimum of the number's occurrences in `arr` and `k`.
#Overall this is what the function does:The function takes a list of integers `arr` and an integer `k`, and returns a dictionary where each key is a unique number from `arr`, and each value is the minimum of the number's occurrences in `arr` and `k`.


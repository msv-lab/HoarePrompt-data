#State of the program right berfore the function call: arr is a list of integers where each integer represents the number written on a card, and k is an integer representing the number of cards to exchange during each operation such that 1 <= len(arr) <= 100 and 2 <= k <= 100. The input consists of multiple test cases, where the first integer t (1 <= t <= 500) indicates the number of test cases, and each test case is described by two lines: the first line contains two integers n and k, and the second line contains n integers representing the numbers on the cards.
def func_1(arr, k):
    frequency_table = {}
    for num in arr:
        frequency_table[num] = frequency_table.get(num, 0) + 1
        
        if frequency_table[num] > k:
            frequency_table[num] = k
        
    #State: `arr` is unchanged, `k` is unchanged, and `frequency_table` is a dictionary with each unique number from `arr` as keys and their counts (capped at `k`) as values.
    return frequency_table
    #The program returns `frequency_table`, which is a dictionary with each unique number from `arr` as keys and their counts (capped at `k`) as values.
#Overall this is what the function does:The function accepts a list of integers `arr` and an integer `k`. It returns a dictionary where each unique number from `arr` is a key, and its value is the count of that number in `arr`, capped at `k`.


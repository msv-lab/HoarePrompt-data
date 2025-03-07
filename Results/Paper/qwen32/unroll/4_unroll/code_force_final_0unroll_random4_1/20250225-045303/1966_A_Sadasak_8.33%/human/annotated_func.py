#State of the program right berfore the function call: arr is a list of integers where each integer represents the number written on a card, and k is an integer such that 2 <= k <= 100. The length of arr is n, where 1 <= n <= 100. The function is expected to handle multiple test cases, each with its own n and k values, and a corresponding list arr of length n.
def func_1(arr, k):
    frequency_table = {}
    for num in arr:
        frequency_table[num] = frequency_table.get(num, 0) + 1
        
        if frequency_table[num] > k:
            frequency_table[num] = k
        
    #State: `arr` is a list of integers where each integer represents the number written on a card, `k` is an integer such that 2 <= k <= 100, the length of `arr` is `n`, where 1 <= n <= 100, and `frequency_table` is a dictionary where each key is a unique integer from `arr` and each value is the minimum of the count of that integer in `arr` and `k`.
    return frequency_table
    #The program returns `frequency_table`, which is a dictionary where each key is a unique integer from the list `arr`, and each value is the minimum of the count of that integer in `arr` and `k`.
#Overall this is what the function does:The function takes a list of integers `arr` and an integer `k`, and returns a dictionary where each key is a unique integer from `arr`, and each value is the minimum of the count of that integer in `arr` and `k`.


#State of the program right berfore the function call: arr is a list of integers where each integer is between 1 and 100 inclusive, and k is an integer such that 2 <= k <= 100. The function is called multiple times for different test cases, each with its own arr and k, where the number of test cases t satisfies 1 <= t <= 500, the length of arr n satisfies 1 <= n <= 100, and arr contains exactly n integers.
def func_1(arr, k):
    frequency_table = {}
    for num in arr:
        frequency_table[num] = frequency_table.get(num, 0) + 1
        
        if frequency_table[num] > k:
            frequency_table[num] = k
        
    #State: `frequency_table` is a dictionary where each key is a unique integer from the list `arr` and the corresponding value is the count of that integer in `arr`, capped at `k`.
    return frequency_table
    #The program returns `frequency_table`, which is a dictionary where each key is a unique integer from the list `arr` and the corresponding value is the count of that integer in `arr`, capped at `k`.
#Overall this is what the function does:The function `func_1` takes a list of integers `arr` and an integer `k` as input. It returns a dictionary where each key is a unique integer from `arr`, and the corresponding value is the count of that integer in `arr`, with the count not exceeding `k`.


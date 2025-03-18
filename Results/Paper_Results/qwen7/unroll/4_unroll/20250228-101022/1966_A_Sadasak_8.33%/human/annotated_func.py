#State of the program right berfore the function call: arr is a list of integers representing the numbers on the cards, and k is an integer such that 2 <= k <= 100.
def func_1(arr, k):
    frequency_table = {}
    for num in arr:
        frequency_table[num] = frequency_table.get(num, 0) + 1
        
        if frequency_table[num] > k:
            frequency_table[num] = k
        
    #State: Output State: The `frequency_table` is a dictionary where each key is a number from the list `arr`, and its value is the maximum occurrence of that number up to `k`. If any number's occurrence exceeds `k`, it is capped at `k`. All other keys not present in `arr` remain absent from the dictionary.
    return frequency_table
    #The program returns the dictionary `frequency_table` which contains each number from the list `arr` as a key, and the maximum occurrence of that number up to `k` as its value. If any number's occurrence exceeds `k`, it is capped at `k`. All other keys not present in `arr` remain absent from the dictionary.
#Overall this is what the function does:The function accepts a list of integers `arr` and an integer `k`. It returns a dictionary `frequency_table` where each key is a number from `arr`, and its value is the maximum occurrence of that number up to `k`. If any number's occurrence exceeds `k`, it is capped at `k`. All other keys not present in `arr` are excluded from the dictionary.


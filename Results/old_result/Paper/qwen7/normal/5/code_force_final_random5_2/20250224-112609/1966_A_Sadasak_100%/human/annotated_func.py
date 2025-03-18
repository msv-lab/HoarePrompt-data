#State of the program right berfore the function call: arr is a list of integers representing the numbers on the cards, and k is an integer such that 2 <= k <= 100.
def func_1(arr, k):
    frequency_table = {}
    for num in arr:
        frequency_table[num] = frequency_table.get(num, 0) + 1
        
        if frequency_table[num] > k:
            frequency_table[num] = k
        
    #State: Output State: After the loop executes all its iterations, `arr` is an empty list, `num` is not defined (since the loop has finished), and `frequency_table` is a dictionary where each key is an integer from the original `arr` that appeared more than `k` times, and its value is set to `k`.
    #
    #This means that every number in the original list `arr` that appeared more than `k` times will have its count capped at `k` in the `frequency_table`. All other numbers that did not appear more than `k` times will not be present in the `frequency_table`.
    return frequency_table
    #The program returns a dictionary named `frequency_table` where each key is an integer from the original `arr` that appeared more than `k` times, and its value is set to `k`. All other numbers that did not appear more than `k` times are not present in the `frequency_table`.
#Overall this is what the function does:The function accepts a list of integers `arr` and an integer `k`. It returns a dictionary `frequency_table` where each key is an integer from `arr` that appears more than `k` times, and its value is set to `k`. Integers that do not appear more than `k` times are not included in the `frequency_table`.


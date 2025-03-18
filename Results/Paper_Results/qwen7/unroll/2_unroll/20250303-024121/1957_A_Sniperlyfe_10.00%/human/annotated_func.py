#State of the program right berfore the function call: arr is a list of integers where each integer represents the length of a stick, and the length of the list is the number of sticks available (1 <= n <= 100). Each stick length is a positive integer not exceeding 100.
def func_1(arr):
    freq = {}
    for n in arr:
        freq[n] = freq.get(n, 0) + 1
        
    #State: Output State: The `freq` dictionary contains key-value pairs where each key is a unique stick length from the `arr` list, and the corresponding value is the frequency (count) of that stick length in the original list.
    return sum(v // 4 for v in freq.values())
    #The program returns the sum of the integer division of each frequency by 4, where each frequency is the count of a unique stick length in the original list.
#Overall this is what the function does:The function accepts a list of integers representing the lengths of sticks. It calculates the frequency of each unique stick length in the list, then returns the sum of these frequencies divided by 4.


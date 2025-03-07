#State of the program right berfore the function call: arr is a list of integers where each integer represents the length of a stick, and the length of the list is the number of sticks available (1 <= n <= 100). Each stick length is a positive integer not exceeding 100.
def func_1(arr):
    freq = {}
    for n in arr:
        freq[n] = freq.get(n, 0) + 1
        
    #State: Output State: The dictionary `freq` will contain each unique stick length from the list `arr` as keys, and their respective counts as values.
    #
    #In Natural Language: After all iterations of the loop, the `freq` dictionary will have been populated with each distinct stick length found in the original list `arr`, and the value for each key will represent how many times that particular stick length appeared in the list.
    return sum(v // 4 for v in freq.values())
    #The program returns the sum of the integer division of each value in the `freq` dictionary by 4.
#Overall this is what the function does:The function accepts a list of integers representing the lengths of sticks. It calculates the frequency of each stick length, then returns the sum of each frequency divided by 4.


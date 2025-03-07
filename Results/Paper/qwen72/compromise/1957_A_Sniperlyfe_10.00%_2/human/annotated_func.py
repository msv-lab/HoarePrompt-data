#State of the program right berfore the function call: arr is a list of integers where each integer represents the length of a stick, and the length of arr is between 1 and 100 inclusive.
def func_1(arr):
    freq = {}
    for n in arr:
        freq[n] = freq.get(n, 0) + 1
        
    #State: `freq` is a dictionary where the keys are the unique integers from the list `arr`, and the values are the counts of how many times each integer appears in `arr`.
    return sum(v // 4 for v in freq.values())
    #The program returns the sum of the integer division of each value in the `freq` dictionary by 4. Each value in `freq` represents the count of how many times a unique integer appears in the list `arr`.
#Overall this is what the function does:The function `func_1` accepts a list `arr` of integers where each integer represents the length of a stick, and the length of `arr` is between 1 and 100 inclusive. It returns the sum of the integer division of the frequency of each unique integer in `arr` by 4. This means the function calculates how many complete sets of 4 sticks can be formed for each unique stick length and returns the total number of such sets.


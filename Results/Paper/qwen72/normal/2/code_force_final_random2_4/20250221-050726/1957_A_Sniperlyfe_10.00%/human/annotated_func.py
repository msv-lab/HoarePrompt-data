#State of the program right berfore the function call: arr is a list of integers where 1 <= len(arr) <= 100 and 1 <= arr[i] <= 100.
def func_1(arr):
    freq = {}
    for n in arr:
        freq[n] = freq.get(n, 0) + 1
        
    #State: `arr` is a list of integers where 1 <= len(arr) <= 100 and 1 <= arr[i] <= 100, `freq` is a dictionary where each key is an integer from `arr` and its value is the count of how many times that integer appears in `arr`.
    return sum(v // 4 for v in freq.values())
    #The program returns the sum of the integer division of each value in the `freq` dictionary by 4. Each value in `freq` represents the count of how many times an integer appears in the list `arr`.
#Overall this is what the function does:The function `func_1` takes a list of integers `arr` (where the length of `arr` is between 1 and 100, and each element is between 1 and 100) and returns the sum of the integer division of the frequency of each unique integer in `arr` by 4. The function does not modify the input list `arr`. After the function concludes, the input list remains unchanged, and the returned value is the computed sum.


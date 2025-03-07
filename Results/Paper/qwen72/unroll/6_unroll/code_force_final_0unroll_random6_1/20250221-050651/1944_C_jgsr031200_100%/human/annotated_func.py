#State of the program right berfore the function call: arr is a list of non-negative integers where each integer is less than the length of the list, and the length of arr is between 1 and 2 * 10^5.
def func_1(arr):
    freq = [0] * (n + 1)
    for i in arr:
        freq[i] += 1
        
    #State: `freq` is a list where each element at index `i` represents the count of occurrences of the integer `i` in the list `arr`. The length of `freq` remains `n + 1`.
    cou = 0
    for i in range(n + 1):
        if freq[i] >= 2:
            continue
        
        if freq[i] == 1:
            cou += 1
        
        if cou == 2 or freq[i] == 0:
            print(i)
            break
        
    #State: `i` is the index where the loop prints and breaks, `cou` is either 0, 1, or 2, and `freq` remains unchanged.
#Overall this is what the function does:The function `func_1` accepts a list `arr` of non-negative integers, where each integer is less than the length of the list, and the length of `arr` is between 1 and 2 * 10^5. It calculates the frequency of each integer in `arr` and then prints the first integer `i` that either has a frequency of 1 and is the second such integer encountered, or the first integer `i` that has a frequency of 0. The function does not return any value, and the list `arr` remains unchanged.


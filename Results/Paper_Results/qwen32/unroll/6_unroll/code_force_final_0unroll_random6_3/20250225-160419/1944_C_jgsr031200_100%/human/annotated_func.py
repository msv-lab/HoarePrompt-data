#State of the program right berfore the function call: arr is a list of integers where each integer a_i satisfies 0 <= a_i < n, and n is the length of arr. The function will be called multiple times with different arrays, and the sum of all n values across these arrays does not exceed 2 * 10^5.
def func_1(arr):
    freq = [0] * (n + 1)
    for i in arr:
        freq[i] += 1
        
    #State: `arr` is a list of integers where each integer `a_i` satisfies 0 <= `a_i` < `n`, and `n` is the length of `arr`. `freq` is a list of integers of length `n + 1`, where each index `j` of `freq` contains the count of how many times the integer `j` appears in `arr`.
    cou = 0
    for i in range(n + 1):
        if freq[i] >= 2:
            continue
        
        if freq[i] == 1:
            cou += 1
        
        if cou == 2 or freq[i] == 0:
            print(i)
            break
        
    #State: `arr` is a list of integers where each integer `a_i` satisfies 0 <= `a_i` < `n`, `freq` is a list of integers of length `n + 1` where `freq[j]` is the count of how many times the integer `j` appears in `arr`, and `cou` is 2 if the loop breaks after finding the second unique element or the value of `cou` before the loop breaks if it encounters a zero frequency element first. The loop prints the value of `i` at the point of breaking.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` where each integer is between 0 and `n-1` (inclusive), with `n` being the length of the list. It prints the smallest integer that either appears exactly once in `arr` or does not appear at all, stopping after finding the second unique element or encountering a zero frequency element.


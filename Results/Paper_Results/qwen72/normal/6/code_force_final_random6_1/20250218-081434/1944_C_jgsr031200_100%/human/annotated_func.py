#State of the program right berfore the function call: arr is a list of non-negative integers where 0 <= arr[i] < len(arr) for all i, and the length of arr is n (1 <= n <= 2 * 10^5).
def func_1(arr):
    freq = [0] * (n + 1)
    for i in arr:
        freq[i] += 1
        
    #State: `arr` is a list of non-negative integers where 0 <= `arr[i]` < len(`arr`) for all i, and the length of `arr` is `n` (1 <= `n` <= 2 * 10^5). `freq` is a list of length `n + 1` where each element `freq[j]` represents the number of times the integer `j` appears in `arr`.
    cou = 0
    for i in range(n + 1):
        if freq[i] >= 2:
            continue
        
        if freq[i] == 1:
            cou += 1
        
        if cou == 2 or freq[i] == 0:
            print(i)
            break
        
    #State: The loop has completed all iterations, and the final state is as follows: `arr` is a list of non-negative integers where `0 <= arr[i] < len(arr)` for all `i`, and the length of `arr` is `n` (1 <= `n` <= 2 * 10^5). `freq` is a list of length `n + 1` where each element `freq[j]` represents the number of times the integer `j` appears in `arr`. `i` is `n`, `cou` is 0, 1, or 2. If the loop did not break early, `cou` is 0 or 1, and no integer `j` in the range `[0, n]` has a frequency of 0 or 2. If the loop broke early, `cou` is 2 or `freq[i]` is 0 for some `i` in the range `[0, n]`.
#Overall this is what the function does:The function `func_1` accepts a list `arr` of non-negative integers, where each integer is less than the length of the list, and the list's length is between 1 and 200,000. It prints the first integer `i` in the range `[0, n]` that either appears exactly once in `arr` (if there are at least two such integers) or the first integer that does not appear in `arr` (if there are fewer than two integers that appear exactly once). If the loop completes without finding such an integer, it prints the last integer in the range `[0, n]` that has a frequency of 0 or 1. The function does not return any value.


#State of the program right berfore the function call: arr is a list of non-negative integers where the length of arr is n (1 ≤ n ≤ 2 · 10^5) and each element a_i in arr satisfies 0 ≤ a_i < n. The function is called multiple times for different test cases, with the total sum of n across all test cases not exceeding 2 · 10^5.
def func_1(arr):
    freq = [0] * (n + 1)
    for i in arr:
        freq[i] += 1
        
    #State: `freq` is a list where each index `j` from 0 to `n` contains the count of how many times `j` appears in the list `arr`.
    cou = 0
    for i in range(n + 1):
        if freq[i] >= 2:
            continue
        
        if freq[i] == 1:
            cou += 1
        
        if cou == 2 or freq[i] == 0:
            print(i)
            break
        
    #State: `freq` remains unchanged, `cou` is either 1 or 2, and the loop prints the first index `i` that either causes `cou` to reach 2 or has a frequency of 0.
#Overall this is what the function does:The function `func_1` takes a list of non-negative integers `arr` as input, where each integer is less than the length of the list `n`. It prints the smallest integer between 0 and `n` that either does not appear in `arr` or appears exactly once.


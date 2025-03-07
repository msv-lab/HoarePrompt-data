#State of the program right berfore the function call: arr is a list of non-negative integers where each integer \(a_i\) satisfies \(0 \le a_i < n\) and the length of the list is \(n\), with \(1 \le n \le 2 \cdot 10^5\).
def func_1(arr):
    freq = [0] * (n + 1)
    for i in arr:
        freq[i] += 1
        
    #State: Output State: `freq` is a list where each index `i` (where \(0 \le i < n\)) contains the count of how many times `i` appears in the original list `arr`. All other elements in `freq` up to index `n` are still zeros.
    cou = 0
    for i in range(n + 1):
        if freq[i] >= 2:
            continue
        
        if freq[i] == 1:
            cou += 1
        
        if cou == 2 or freq[i] == 0:
            print(i)
            break
        
    #State: Output State: `cou` is 0, `freq` is a list where each index `i` (where \(0 \le i < n\)) contains the count of how many times `i` appears in the original list `arr`, and no elements in the list are printed.
#Overall this is what the function does:The function accepts a list of non-negative integers `arr` and returns nothing. It counts the frequency of each integer in `arr` and prints an integer `i` (where \(0 \le i < n\)) if `i` appears exactly once in `arr` and there are fewer than two such integers. If there are two or more such integers, it prints the first one found. If no such integer exists, it prints nothing.


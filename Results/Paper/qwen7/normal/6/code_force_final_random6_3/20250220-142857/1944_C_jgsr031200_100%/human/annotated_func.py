#State of the program right berfore the function call: arr is a list of non-negative integers where each integer \(a_i\) satisfies \(0 \le a_i < n\) and the length of the list is \(n\), with \(1 \le n \le 2 \cdot 10^5\).
def func_1(arr):
    freq = [0] * (n + 1)
    for i in arr:
        freq[i] += 1
        
    #State: Output State: The `freq` list will contain the count of how many times each index from 0 to n (where n is the length of the `arr` list) appears in the `arr` list.
    #
    #In more detail, after all iterations of the loop have finished, the `freq` list will reflect the frequency of each integer in the `arr` list. Specifically, if the integer `j` appears `k` times in the `arr` list, then `freq[j]` will be equal to `k`. All other elements in the `freq` list (those indices that do not appear in `arr`) will remain as 0.
    cou = 0
    for i in range(n + 1):
        if freq[i] >= 2:
            continue
        
        if freq[i] == 1:
            cou += 1
        
        if cou == 2 or freq[i] == 0:
            print(i)
            break
        
    #State: The loop has executed all its iterations, and the final value of `i` is `n`. The variable `cou` remains 0 throughout the loop's execution.
#Overall this is what the function does:The function accepts a list of non-negative integers `arr` and calculates the frequency of each integer in the list. It then iterates through these frequencies, printing the first integer that appears exactly once or not at all, and stops after finding two such integers. If no such integers are found, it prints nothing.


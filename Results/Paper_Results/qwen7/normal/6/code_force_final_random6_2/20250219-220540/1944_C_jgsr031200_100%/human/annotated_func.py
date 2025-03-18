#State of the program right berfore the function call: arr is a list of non-negative integers where each integer \(a_i\) satisfies \(0 \le a_i < n\), and \(n\) is a positive integer such that \(1 \le n \le 2 \cdot 10^5\).
def func_1(arr):
    freq = [0] * (n + 1)
    for i in arr:
        freq[i] += 1
        
    #State: Output State: The list `arr` has been fully iterated over, and for each element `i` in `arr`, the corresponding value `freq[i]` in the `freq` list has been incremented by 1 for each occurrence of `i` in `arr`. Therefore, `freq` now contains the frequency count of each integer that appeared in `arr`.
    cou = 0
    for i in range(n + 1):
        if freq[i] >= 2:
            continue
        
        if freq[i] == 1:
            cou += 1
        
        if cou == 2 or freq[i] == 0:
            print(i)
            break
        
    #State: The loop has executed all its iterations, meaning `i` has reached `n+1`. The value of `cou` is either 0 or 1, depending on how many times `freq[i]` was 1 during the loop's execution. The variable `n` remains unchanged from its initial value. If at any point `freq[i]` was 0, the loop would have broken early, and if `freq[i]` was greater than or equal to 2, the loop would have continued without breaking.
#Overall this is what the function does:The function accepts a list `arr` of non-negative integers where each integer \(a_i\) satisfies \(0 \le a_i < n\), and \(n\) is a positive integer such that \(1 \le n \le 2 \cdot 10^5\). It calculates the frequency of each integer in `arr` and prints the first integer `i` in the range \(0\) to \(n\) that appears exactly once in `arr`. If no such integer exists, it prints nothing. The function does not return any value.


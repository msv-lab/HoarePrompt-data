#State of the program right berfore the function call: n and k are integers such that 1 ≤ k ≤ n ≤ 5000, and a is a list of n integers where each a_i satisfies 1 ≤ a_i ≤ 5000.
def func():
    n, k = map(int, raw_input().split())
    arr = map(int, raw_input().split())
    max_avg = 0
    for i in range(k, n + 1):
        cur = sum(arr[:i])
        
        cur_max = cur
        
        for j in range(i, n):
            cur = cur - arr[j - i] + arr[j]
            if cur > cur_max:
                cur_max = cur
        
        if cur_max / float(i) > max_avg:
            max_avg = cur_max / float(i)
        
    #State of the program after the  for loop has been executed: `n` and `k` are integers such that \(1 \leq k \leq n \leq 5000\), `a` is a list of `n` integers where each `a_i` satisfies \(1 \leq a_i \leq 5000\), `arr` is an iterable of integers read from the input, `i` is `n + 1`, `cur` is the sum of the last `n` elements of `arr`, `cur_max` is the maximum sum of any contiguous subarray of length `n` in `arr`. `max_avg` is the maximum average of any contiguous subarray of length `k` to `n` in `arr`.
    print(max_avg)
#Overall this is what the function does:The function reads two integers `n` and `k` from the input, followed by a list of `n` integers `arr`. It then calculates the maximum average of any contiguous subarray of length between `k` and `n` (inclusive). The function prints this maximum average to the standard output. After the function concludes, the state of the program includes the original values of `n` and `k`, the list `arr`, and the calculated maximum average. Note that the function does not return any value; it only prints the result. Edge cases include scenarios where `k` equals `n` (the entire array is considered), and when `k` is 1 (every single element is a subarray of length 1). The function handles these cases correctly. However, the function does not validate the input constraints (e.g., ensuring `1 ≤ k ≤ n ≤ 5000` and `1 ≤ a_i ≤ 5000`), which could lead to unexpected behavior if the input is invalid.


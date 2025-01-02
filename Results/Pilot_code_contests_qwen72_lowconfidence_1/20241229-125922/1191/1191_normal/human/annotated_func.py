#State of the program right berfore the function call: n, k, and x are integers such that 1 ≤ k, x ≤ n ≤ 200, and a list a of n integers where 1 ≤ a_i ≤ 10^9.
def func():
    sys.stdin = BytesIO(sys.stdin.read())
    input = lambda : sys.stdin.readline().rstrip('\r\n')
    n, k, x = [int(_) for _ in input().split()]
    arr = [int(_) for _ in input().split()]
    if (k > 1) :
        rpr = {(x, 1): 0, (x - 1, 0): arr[0]}
    else :
        rpr = {(x - 1, 0): arr[0]}
    #State of the program after the if-else block has been executed: *`n`, `k`, and `x` are integers such that 1 ≤ k, x ≤ n ≤ 200, `a` is a list of `n` integers where 1 ≤ a_i ≤ 10^9, `arr` is a list of integers read from the next line of input. If `k` > 1, `rpr` is a dictionary with two key-value pairs: `{(x, 1): 0, (x - 1, 0): arr[0]}`. If `k` is exactly 1, `rpr` is a dictionary with a single key-value pair: `{(x - 1, 0): arr[0]}`.
    i = 1
    while i < n and len(rpr):
        pr = defaultdict(int)
        
        for ost, lag in rpr:
            if lag + 1 == k:
                if ost > 0:
                    pr[ost - 1, 0] = max(pr[ost - 1, 0], rpr[ost, lag] + arr[i])
                else:
                    continue
            else:
                pr[ost, lag + 1] = max(pr[ost, lag + 1], rpr[ost, lag])
                if ost > 0:
                    pr[ost - 1, 0] = max(pr[ost - 1, 0], rpr[ost, lag] + arr[i])
        
        rpr = dict()
        
        for ke in pr:
            rpr[ke] = pr[ke]
        
        i += 1
        
    #State of the program after the loop has been executed: `n` is an integer such that 1 ≤ n ≤ 200, `k` and `x` are integers such that 1 ≤ k, x ≤ n, `a` is a list of `n` integers where 1 ≤ a_i ≤ 10^9, `arr` is a list of integers read from the next line of input, `i` is `n`, `rpr` is a dictionary containing the final key-value pairs computed from the loop, where each key is a tuple `(ost, lag)` and each value is the maximum value computed based on the conditions described in the loop.
    if len(rpr) :
        m = 0
        for k in rpr:
            m = max(m, rpr[k])
            
        #State of the program after the  for loop has been executed: To determine the output state after all iterations of the loop have finished, we need to consider the following:
        #
        #1. **Initial State**: 
        #   - `n` is an integer such that 1 ≤ n ≤ 200
        #   - `k` and `x` are integers such that 1 ≤ k, x ≤ n
        #   - `a` is a list of `n` integers where 1 ≤ a_i ≤ 10^9
        #   - `arr` is a list of integers read from the next line of input
        #   - `rpr` is a dictionary containing the final key-value pairs computed from the loop, where each key is a tuple `(ost, lag)` and each value is the maximum value computed based on the conditions described in the loop, and the length of `rpr` is greater than 0
        #   - `m` is 0
        #
        #2. **Loop Code**:
        #   ```python
        #   for k in rpr:
        #       m = max(m, rpr[k])
        #   ```
        #
        #3. **Output State After All Iterations**:
        #   - The loop iterates over each key `k` in the dictionary `rpr`.
        #   - For each key `k`, the value `rpr[k]` is compared to the current value of `m`, and `m` is updated to the maximum of these two values.
        #   - This process continues until all keys in `rpr` have been processed.
        #
        #Given the above, after all iterations of the loop have finished:
        #
        #- `n` remains an integer such that 1 ≤ n ≤ 200
        #- `k` is the last key processed in the iteration order of `rpr`
        #- `x` remains an integer such that 1 ≤ x ≤ n
        #- `a` remains a list of `n` integers where 1 ≤ a_i ≤ 10^9
        #- `arr` remains a list of integers read from the next line of input
        #- `rpr` remains a dictionary containing the final key-value pairs computed from the loop, where each key is a tuple `(ost, lag)` and each value is the maximum value computed based on the conditions described in the loop, and the length of `rpr` is greater than 0
        #- `m` is the maximum value among all values in `rpr`
        #
        #Therefore, the output state is:
        #**`n` is an integer such that 1 ≤ n ≤ 200, `k` is the last key processed in the iteration order of `rpr`, `x` is an integer such that 1 ≤ x ≤ n, `a` is a list of `n` integers where 1 ≤ a_i ≤ 10^9, `arr` is a list of integers read from the next line of input, `rpr` is a dictionary containing the final key-value pairs computed from the loop, where each key is a tuple `(ost, lag)` and each value is the maximum value computed based on the conditions described in the loop, the length of `rpr` is greater than 0, `m` is the maximum value among all values in `rpr`**.
        print(m)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`n` is an integer such that 1 ≤ n ≤ 200, `k` and `x` are integers such that 1 ≤ k, x ≤ n, `a` is a list of `n` integers where 1 ≤ a_i ≤ 10^9, `arr` is a list of integers read from the next line of input, `i` is `n`, `rpr` is a dictionary containing the final key-value pairs computed from the loop, where each key is a tuple `(ost, lag)` and each value is the maximum value computed based on the conditions described in the loop. If the length of `rpr` is greater than 0, `k` is the last key processed in the iteration order of `rpr`, `m` is the maximum value among all values in `rpr`, and the value of `m` is printed. If the length of `rpr` is 0, `-1` has been printed.
#Overall this is what the function does:The function reads input values `n`, `k`, and `x` followed by a list of `n` integers `arr`. It then processes the list `arr` to compute a dictionary `rpr` that tracks certain states based on the values in `arr` and the constraints defined by `k` and `x`. The function iterates through the list `arr` and updates the dictionary `rpr` according to specific rules. After processing, it finds the maximum value in `rpr` and prints it if `rpr` is not empty; otherwise, it prints `-1`. The function does not return any value but prints the result directly. The final state of the program includes the variables `n`, `k`, `x`, and `arr` remaining unchanged, and the dictionary `rpr` containing the final computed key-value pairs. If `rpr` is not empty, the maximum value in `rpr` is printed; otherwise, `-1` is printed.


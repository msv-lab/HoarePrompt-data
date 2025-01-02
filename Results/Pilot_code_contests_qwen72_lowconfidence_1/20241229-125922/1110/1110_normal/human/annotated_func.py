#State of the program right berfore the function call: The function `func` is intended to process multiple test cases, each involving a sequence of digits. The input includes an integer `t` representing the number of test cases, followed by `t` test cases. Each test case consists of an integer `n` (1 ≤ n ≤ 2⋅10^5) indicating the length of the digit sequence, and a string of `n` digits (0-9). The sum of `n` across all test cases does not exceed 2⋅10^5.
def func():
    g = lambda : stdin.readline().strip()
    gl = lambda : g().split()
    gil = lambda : [int(var) for var in gl()]
    gfl = lambda : [float(var) for var in gl()]
    gcl = lambda : list(g())
    gbs = lambda : [int(var) for var in g()]
    mod = int(1000000000.0) + 7
    inf = float('inf')
    t, = gil()
    for _ in range(t):
        n, = gil()
        
        val = gbs()
        
        idx = list(xrange(n))
        
        idx.sort(key=lambda x: [val[x], x])
        
        one = []
        
        to = []
        
        for ix in idx:
            if ix > (one[-1] if one else -1) and val[ix] <= (val[to[0]] if to else inf
                ):
                one.append(ix)
            elif ix > (to[-1] if to else -1):
                to.append(ix)
            else:
                break
        
        if len(one) + len(to) == n:
            for ix in one:
                val[ix] = 1
            for ix in to:
                val[ix] = 2
            for v in val:
                print(v, end='')
            print()
        else:
            print('-')
        
    #State of the program after the  for loop has been executed: `_` is incremented by `t` (the number of iterations specified by `t`), `one` is a list of indices from `idx` that satisfy the condition `ix > (one[-1] if one else -1) and val[ix] <= (val[to[0]] if to else inf)`, `to` is a list of indices from `idx` that satisfy the condition `ix > (to[-1] if to else -1)` and do not satisfy the condition for `one`, `idx` is a sorted list of indices based on `val`, `val` is a list of integers, `n` is the length of `val`, `inf` is `float('inf')`, and all other variables remain unchanged from their initial values. For each iteration, if the combined length of `one` and `to` is equal to `n`, then `one` is a non-empty list and `val[ix] = 1` for all `ix` in `one` and `val[ix] = 2` for all `ix` in `to`. The values in `val` are printed without newline characters, followed by a newline character. If the combined length of `one` and `to` is less than `n` for any iteration, a single hyphen (`-`) is printed. After all iterations, `one` and `to` are reset for each new iteration, and the final state of `val` depends on the last iteration where `len(one) + len(to) == n`. If no such iteration exists, `val` retains its original value for each iteration.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by an integer `n` (1 ≤ n ≤ 2⋅10^5) and a string of `n` digits (0-9). For each test case, it attempts to partition the digits into two groups: `one` and `to`. The group `one` contains indices where the current digit is greater than the previous digit in `one` and less than or equal to the first digit in `to` (if `to` is not empty). The group `to` contains indices where the current digit is greater than the previous digit in `to` and does not meet the conditions for `one`. If the combined length of `one` and `to` equals `n`, the function prints the modified sequence where digits at indices in `one` are set to 1 and digits at indices in `to` are set to 2. If the combined length of `one` and `to` is less than `n`, the function prints a hyphen (`-`). The function processes `t` test cases, where `t` is the number of test cases provided as input. After processing all test cases, the function does not return any value; it only prints the results for each test case. Potential edge cases include scenarios where the input sequence is empty or contains all identical digits, which might affect the partitioning logic.


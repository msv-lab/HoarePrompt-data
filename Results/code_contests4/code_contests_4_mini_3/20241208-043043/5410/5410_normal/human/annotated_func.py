#State of the program right berfore the function call: N is a positive integer such that 1 <= N <= 50, A and B are integers such that 1 <= A, B <= N, and v_i are integers such that 1 <= v_i <= 10^{15} for each i in the range 1 to N. The input values for v_i are provided in a sequence following the first line of input.
def func():
    N, A, B = map(int, raw_input().split())
    v = map(int, raw_input().split())
    resultValue = 0
    resultCount = 0
    for pcs in range(B - A + 1):
        perm = list(itertools.combinations(v, B + pcs))
        
        for cand in perm:
            average = float(sum(cand)) / len(cand)
            if resultValue < average:
                resultValue = average
                resultCount = 1
            elif resultValue == average:
                resultCount += 1
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 <= `N` <= 50; `A` is an integer such that 1 <= `A` <= `N`; `B` is an integer such that 1 <= `B` <= `N`; `resultValue` is the maximum average of all combinations of `v` taken `B + pcs` at a time for `pcs` in the range from 0 to `B - A`; `resultCount` is the number of combinations that produced the maximum average across all iterations; `pcs` is `B - A`.
    print(resultValue)
    print(resultCount)
#Overall this is what the function does:The function accepts three integers `N`, `A`, and `B`, and a list of integers `v`. It calculates the maximum average of all combinations of the integers in `v` taken `B + pcs` at a time for `pcs` in the range from `0` to `B - A`, and counts how many combinations yield that maximum average, returning these two values.


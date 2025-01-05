#State of the program right berfore the function call: N is a positive integer such that 1 <= N <= 50, A and B are integers such that 1 <= A, B <= N, and v_i are integers such that 1 <= v_i <= 10^15 for each i (1 <= i <= N).
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
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 <= `N` <= 50; `A` and `B` are integers such that 1 <= `A`, `B` <= `N`; `B` is greater than or equal to `A`; `resultValue` is the maximum average of all combinations of `v` taken `B + pcs` at a time for `pcs` in the range from 0 to `B - A`; `resultCount` is the count of combinations that yield the `resultValue`.
    print(resultValue)
    print(resultCount)
#Overall this is what the function does:The function accepts input values for N, A, B, and a list of integers v. It calculates the maximum average of all combinations of elements from v taken B + pcs at a time, where pcs varies from 0 to B - A. It then counts how many combinations yield this maximum average. The function outputs the maximum average and the count of combinations that achieve this average. However, it does not handle cases where the input values do not meet the specified constraints, nor does it validate the input.


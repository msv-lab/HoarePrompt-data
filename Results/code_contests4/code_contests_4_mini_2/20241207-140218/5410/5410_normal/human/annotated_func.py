#State of the program right berfore the function call: N is an integer such that 1 <= N <= 50, A and B are integers such that 1 <= A, B <= N, and v_i are integers such that 1 <= v_i <= 10^15 for each item i (1 <= i <= N).
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
        
    #State of the program after the  for loop has been executed: `N`, `A`, and `B` are integers such that 1 <= `N` <= 50; `resultValue` is the maximum average of all candidate combinations evaluated; `resultCount` is the number of candidates that have an average equal to `resultValue`.
    print(resultValue)
    print(resultCount)
#Overall this is what the function does:The function accepts no parameters directly but reads three integers N, A, and B from input, along with a list of integers v_i. It calculates the maximum average of all combinations of the integers in v_i, where the size of each combination ranges from B to B + (B - A). It returns the maximum average found and counts how many combinations yield this maximum average. If no combinations are formed (which can happen if B is greater than the number of available integers), it will still attempt to compute averages, potentially leading to a division by zero error.


#State of the program right berfore the function call: **Precondition**: 
- N, A, B are integers such that 1 <= N <= 50, 1 <= A, B <= N.
- v_i is an integer such that 1 <= v_i <= 10^15 for each i-th item.
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
        
    #State of the program after the  for loop has been executed: `resultValue` will contain the maximum average value calculated from all the combinations in `perm`, `resultCount` will represent the number of times the `resultValue` occurred as the average. All other variables will remain unchanged.
    print(resultValue)
    print(resultCount)
#Overall this is what the function does:The function reads input parameters N, A, B and a list v. It then calculates the average of all combinations of v elements with lengths ranging from B to B + N. The function finds the maximum average value among these combinations and the number of times this maximum value occurs. Finally, it prints the maximum average value and the count of occurrences of this value.


#State of the program right berfore the function call: N, A, B are positive integers such that 1 <= N <= 50, 1 <= A, B <= N. v_i are positive integers such that 1 <= v_i <= 10^15 for each i-th item.**
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
        
    #State of the program after the  for loop has been executed: N is between 1 and 50, A is between 1 and N, B is between 1 and N, B is greater than or equal to A, pcs is B - A + 1, perm is a list of combinations of elements in v with a length of B + pcs and contains at least B - A + 1 combinations, average is the maximum average calculated throughout all combinations in perm, resultValue is the maximum average calculated throughout all combinations in perm, resultCount is the number of times the maximum average occurs in the combinations
    print(resultValue)
    print(resultCount)
#Overall this is what the function does:The function `func` reads input values for N, A, B, and a list of positive integers v. It then calculates the maximum average of combinations of elements from v with lengths ranging from B to B + N. The function prints the maximum average value and the number of times it occurs in the combinations. The function does not return any specific output.


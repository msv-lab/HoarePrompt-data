#State of the program right berfore the function call: N, A, B are positive integers such that 1 <= N <= 50, 1 <= A, B <= N. v_i are integers such that 1 <= v_i <= 10^15 for all i.**
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
        
    #State of the program after the  for loop has been executed: N is the length of v, A is less than or equal to B, resultValue is the maximum average value of elements in the perm list, resultCount is the number of times the maximum average value occurs in the perm list, pcs is adjusted for the last cand and incremented by the total number of elements in perm + 1, cand represents the last element in perm, average is the average value of elements in cand, perm is a list of all combinations of v with length B + pcs
    print(resultValue)
    print(resultCount)
#Overall this is what the function does:The function `func` reads three integers N, A, B, and a list of integers v. It then calculates the maximum average value of elements in different combinations of v with lengths ranging from A to B inclusive. Finally, it prints the maximum average value and the number of times it occurs in the combinations. However, the function does not return any specific value.


#State of the program right berfore the function call: q is a positive integer such that 1 ≤ q ≤ 10^5, and for each query ni is a positive integer such that 1 ≤ ni ≤ 10^9.
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: `a` is the last input value, `c` is either 0 or 1 based on the parity of `a`, outputs are -1 for `a` in (1, 2, 3, 5, 7, 11) or `a / 4 + c` otherwise.
#Overall this is what the function does:The function accepts a positive integer `q`, representing the number of queries, and processes `q` positive integers `a`. For each integer `a`, if it is odd, it subtracts 9 and sets a counter `c` to 1. It then checks if the modified (or unmodified) `a` is in the set {1, 2, 3, 5, 7, 11}, returning -1 for those values. Otherwise, it returns the result of `a / 4 + c`. The function handles up to 100,000 queries, but does not explicitly check the range of `a` for each query, so it assumes valid input as per the problem statement.


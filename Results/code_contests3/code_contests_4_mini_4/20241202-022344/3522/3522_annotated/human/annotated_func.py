#State of the program right berfore the function call: q is a positive integer such that 1 ≤ q ≤ 10^5, and for each query ni, ni is a positive integer such that 1 ≤ ni ≤ 10^9.
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: For each query `a`, if `a` is in (1, 2, 3, 5, 7, 11), the output is -1; if `a` is even and not in (1, 2, 3, 5, 7, 11), the output is `a / 4`; if `a` is odd and not in (1, 2, 3, 5, 7, 11), the output is `(a - 9) / 4 + 1`. `c` is 1 if the original `a` was odd and not in (1, 2, 3, 5, 7, 11), otherwise `c` is 0.
#Overall this is what the function does:The function accepts multiple positive integer queries and processes each query according to specific conditions. For each query `a`, if `a` is in the set {1, 2, 3, 5, 7, 11}, it returns -1. If `a` is even and not in that set, it returns `a / 4`. If `a` is odd and not in that set, it first subtracts 9 from `a`, increments a counter `c` by 1, and then returns `(a - 9) / 4 + 1`. The function handles up to 100,000 queries, and each query value can be as large as 1 billion.


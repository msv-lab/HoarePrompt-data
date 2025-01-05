#State of the program right berfore the function call: q is a positive integer such that 1 ≤ q ≤ 10^5, and for each query ni is a positive integer such that 1 ≤ ni ≤ 10^9.
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: `q` is a positive integer such that 1 ≤ `q` ≤ 10^5, `a` is the last input processed, `c` is 0 if `a` is even or 1 if `a` is odd.
#Overall this is what the function does:The function processes multiple queries where each query is a positive integer `a`. If `a` is odd, it subtracts 9 from `a` and sets a counter `c` to 1. It then checks if the resulting `a` is one of the prime numbers 1, 2, 3, 5, 7, or 11; if it is, it returns -1. Otherwise, it returns the value of `a` divided by 4, plus `c`. The function effectively handles and processes up to 100,000 queries, returning results based on the conditions applied to each query.


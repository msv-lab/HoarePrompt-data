#State of the program right berfore the function call: q is an integer such that 1 ≤ q ≤ 100,000, and ni is a positive integer such that 1 ≤ ni ≤ 1,000,000,000 for each query.
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: `a` is an even number, output is -1 if `a` is one of the numbers 1, 2, 3, 5, 7, 11; otherwise, output is `a / 4 + c`, where `c` is 1 if the original `a` was odd, and 0 if `a` was even.
#Overall this is what the function does:The function accepts an implicit number of queries `q` (1 ≤ q ≤ 100,000) and for each query, it processes a positive integer `a` (1 ≤ a ≤ 1,000,000,000). If `a` is odd, it subtracts 9 from `a` and sets a counter `c` to 1. The function then checks if the resulting `a` is in the set {1, 2, 3, 5, 7, 11}. If it is, the function outputs -1; otherwise, it outputs `a / 4 + c`. The function does not explicitly return any values but prints the result for each query.


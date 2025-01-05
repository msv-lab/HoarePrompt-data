#State of the program right berfore the function call: q is a positive integer such that 1 ≤ q ≤ 100,000, and for each query ni, ni is a positive integer such that 1 ≤ ni ≤ 1,000,000,000.
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: For each input value `a`, if the adjusted `a` is in (1, 2, 3, 5, 7, 11), output is -1; otherwise, output is the result of `a / 4 + c` where `c` is 0 if `a` is even and 1 if `a` is odd after adjustments.
#Overall this is what the function does:The function accepts a positive integer input q, representing the number of queries. For each query, it checks the value of a positive integer a. If a is odd, it subtracts 9 and sets a counter c to 1. It then checks if the adjusted a is in the set (1, 2, 3, 5, 7, 11). If it is, the output is -1; otherwise, it calculates and outputs a / 4 + c. The function processes up to 100,000 queries with values of a that can be as large as 1,000,000,000.


#State of the program right berfore the function call: q is a positive integer such that 1 ≤ q ≤ 10^5, and for each query ni is a positive integer such that 1 ≤ ni ≤ 10^9.
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: `q` is 0, `a` is the last processed positive integer, `c` is either 0 or 1 depending on whether the last `a` was even or odd.
#Overall this is what the function does:The function accepts a positive integer `q` representing the number of queries, where each query consists of a positive integer `a`. For each query, if `a` is odd, it is decreased by 9, and a counter `c` is set to 1. The function then checks if the resulting value of `a` (after potentially being adjusted) is one of the numbers in the set {1, 2, 3, 5, 7, 11}. If it is, the function returns -1. Otherwise, it returns the integer division of `a` by 4 plus the counter `c`. The function will process `q` queries and print the results for each. Edge cases include handling of odd numbers less than or equal to 9, which will result in returning -1, as well as ensuring proper output formatting.


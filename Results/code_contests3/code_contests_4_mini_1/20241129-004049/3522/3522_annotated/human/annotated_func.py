#State of the program right berfore the function call: q is a positive integer such that 1 ≤ q ≤ 10^5, and for each query ni is a positive integer such that 1 ≤ ni ≤ 10^9.
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: `q` is a positive integer such that 1 ≤ `q` ≤ 10^5; for each query, if `a` is an odd integer, it is reduced by 9 and `c` is set to 1; if `a` is even, `c` remains 0; the result printed is -1 if `a` is one of the specified values (1, 2, 3, 5, 7, 11) or `a / 4 + c` otherwise.
#Overall this is what the function does:The function accepts multiple queries defined by a positive integer `q` and processes each query with a positive integer `a`. If `a` is odd, it is reduced by 9 and a counter `c` is set to 1; if `a` is even, `c` remains 0. The function then prints -1 if the adjusted `a` is one of the values (1, 2, 3, 5, 7, 11), or prints the result of `a / 4 + c` otherwise. It handles multiple queries, printing a result for each.

